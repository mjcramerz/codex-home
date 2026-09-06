#!/usr/bin/env python3
"""Build multi-page ADHD/CBT packs from a JSON config."""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
from datetime import date, timedelta
from pathlib import Path
from typing import Any

import render_template

MAX_CONFIG_BYTES = 1_000_000
MAX_TOTAL_PAGES = 200


class ConfigError(Exception):
    pass


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ConfigError(f"Config not found: {path}")
    if not path.is_file():
        raise ConfigError(f"Config is not a file: {path}")
    if path.stat().st_size > MAX_CONFIG_BYTES:
        raise ConfigError("Config file too large")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ConfigError(f"Invalid JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ConfigError("Config must be a JSON object")
    return data


def _resolve_under(base_dir: Path, candidate: Path) -> Path:
    base = base_dir.resolve()
    resolved = (base / candidate).resolve()
    if base != resolved and base not in resolved.parents:
        raise ConfigError(f"Path escapes allowed root {base}: {candidate}")
    return resolved


def resolve_template(path_or_name: str, assets_dir: Path) -> Path:
    candidate = Path(path_or_name)
    if candidate.is_absolute():
        return candidate
    if candidate.suffix != ".html":
        candidate = candidate.with_suffix(".html")
    return _resolve_under(assets_dir / "templates", candidate)


def resolve_css(path_or_name: str | None, assets_dir: Path) -> Path:
    if not path_or_name:
        return (assets_dir / "styles" / "pdf.css").resolve()
    candidate = Path(path_or_name)
    if candidate.is_absolute():
        return candidate
    return _resolve_under(assets_dir, candidate)


def normalize_data(data: Any, data_file: Any) -> dict:
    if data_file and data is not None:
        raise ConfigError("Use either 'data' or 'data_file' per page entry, not both")
    if data_file:
        data_path = Path(data_file)
        return render_template.load_data(data_path.resolve())
    if data is None:
        return {}
    if not isinstance(data, dict):
        raise ConfigError("Page data must be an object")
    return data


def apply_date_fields(base: dict, current: date, force: bool) -> dict:
    merged = dict(base)
    if force or "date" not in merged:
        merged["date"] = current.isoformat()
    if force or "day" not in merged:
        merged["day"] = current.strftime("%A")
    return merged


def build_pages(config: dict, assets_dir: Path) -> str:
    pages = config.get("pages")
    if not isinstance(pages, list) or not pages:
        raise ConfigError("Config must include a non-empty 'pages' list")
    if len(pages) > MAX_TOTAL_PAGES:
        raise ConfigError(f"Too many page definitions (max {MAX_TOTAL_PAGES})")

    html_parts: list[str] = []
    total_pages = 0

    for page in pages:
        if not isinstance(page, dict):
            raise ConfigError("Each page entry must be an object")
        template_key = page.get("template")
        if not template_key:
            raise ConfigError("Each page must include a 'template' field")
        template_path = resolve_template(str(template_key), assets_dir)
        template_text = render_template.read_text(
            template_path.resolve(), render_template.MAX_TEMPLATE_BYTES
        )

        repeat = page.get("repeat", 1)
        if not isinstance(repeat, int) or repeat < 1 or repeat > 31:
            raise ConfigError("repeat must be an integer between 1 and 31")
        total_pages += repeat
        if total_pages > MAX_TOTAL_PAGES:
            raise ConfigError(
                f"Total rendered pages exceed limit ({MAX_TOTAL_PAGES}); reduce repeat/page count"
            )

        start_date_raw = page.get("start_date")
        start_date = None
        if start_date_raw:
            try:
                start_date = date.fromisoformat(str(start_date_raw))
            except ValueError as exc:
                raise ConfigError("start_date must be YYYY-MM-DD") from exc

        force_date = bool(page.get("force_date", False))
        data = normalize_data(page.get("data"), page.get("data_file"))

        for index in range(repeat):
            current_data = dict(data)
            if start_date:
                current_data = apply_date_fields(
                    current_data, start_date + timedelta(days=index), force_date
                )
            rendered = render_template.apply_template(template_text, current_data)
            html_parts.append(rendered)

    return "\n".join(html_parts)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build ADHD/CBT PDF packs")
    parser.add_argument(
        "--config",
        required=True,
        help="JSON config file describing pages",
    )
    parser.add_argument("--out", required=True, help="Output file (.html or .pdf)")
    parser.add_argument(
        "--engine",
        default="auto",
        choices=["auto", "wkhtmltopdf", "weasyprint", "pandoc"],
        help="PDF conversion engine",
    )
    parser.add_argument(
        "--page-size",
        default=render_template.DEFAULT_PAGE_SIZE,
        help="PDF page size (default: A4)",
    )
    parser.add_argument(
        "--margin",
        default=render_template.DEFAULT_MARGIN,
        help="PDF margin for wkhtmltopdf (default: 14mm)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    script_dir = Path(__file__).resolve().parent
    assets_dir = script_dir.parent / "assets"

    try:
        config = read_json(Path(args.config).resolve())
        page_size_raw = config.get("page_size", args.page_size)
        margin_raw = config.get("margin", args.margin)
        page_size, margin = render_template.validate_pdf_options(
            str(page_size_raw), str(margin_raw)
        )
        css_path = resolve_css(config.get("css"), assets_dir)
        css_text = render_template.read_text(
            css_path.resolve(), render_template.MAX_CSS_BYTES
        )
        html = build_pages(config, assets_dir)
        html = render_template.embed_css(html, css_text)
        if len(html.encode("utf-8")) > render_template.MAX_RENDERED_HTML_BYTES:
            raise ConfigError(
                f"Rendered HTML exceeds {render_template.MAX_RENDERED_HTML_BYTES} bytes"
            )

        output_path = Path(args.out).resolve()
        output_suffix = output_path.suffix.lower()
        if output_suffix not in {".html", ".htm", ".pdf"}:
            raise ConfigError("Output must end with .html, .htm, or .pdf")
        output_path.parent.mkdir(parents=True, exist_ok=True)

        if output_suffix != ".pdf":
            output_path.write_text(html, encoding="utf-8")
            return 0

        engine = render_template.find_engine(args.engine)
        if not engine:
            html_fallback = output_path.with_suffix(".html")
            html_fallback.write_text(html, encoding="utf-8")
            raise ConfigError(
                "No PDF engine found. Install wkhtmltopdf, weasyprint, or pandoc. "
                f"HTML saved to {html_fallback}"
            )

        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_html = Path(tmp_dir) / "pack.html"
            tmp_html.write_text(html, encoding="utf-8")
            render_template.convert_html_to_pdf(
                tmp_html,
                output_path,
                engine,
                page_size=page_size,
                margin=margin,
            )

        return 0
    except (ConfigError, render_template.RenderError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
