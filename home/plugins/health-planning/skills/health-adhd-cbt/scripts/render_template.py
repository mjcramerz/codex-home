#!/usr/bin/env python3
"""Render ADHD/CBT templates to HTML or PDF.

Usage:
  render_template.py --template assets/templates/daily-pack.html \
    --css assets/styles/pdf.css \
    --data assets/data/example.json \
    --out /tmp/daily-pack.pdf

Notes:
- PDF rendering uses an external engine if available: wkhtmltopdf, weasyprint, or pandoc.
- If no engine is found, the script writes HTML instead and exits non-zero.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any
from string import Template

MAX_TEMPLATE_BYTES = 2_000_000
MAX_DATA_BYTES = 1_000_000
MAX_CSS_BYTES = 1_000_000
MAX_RENDERED_HTML_BYTES = 8_000_000
MAX_DATA_KEYS = 512
MAX_KEY_CHARS = 64
MAX_VALUE_CHARS = 20_000
CONVERT_TIMEOUT_SEC = 60
DEFAULT_PAGE_SIZE = "A4"
DEFAULT_MARGIN = "14mm"
MAX_COMMAND_ERROR_CHARS = 1200

PLACEHOLDER_KEY_PATTERN = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
PAGE_SIZE_PATTERN = re.compile(r"^[A-Za-z0-9_-]{1,20}$")
MARGIN_PATTERN = re.compile(r"^[0-9]{1,3}(?:\\.[0-9]{1,2})?(?:mm|cm|in|pt|px)$")


class RenderError(Exception):
    pass


def read_text(path: Path, max_bytes: int) -> str:
    if not path.exists():
        raise RenderError(f"File not found: {path}")
    if not path.is_file():
        raise RenderError(f"Not a file: {path}")
    size = path.stat().st_size
    if size > max_bytes:
        raise RenderError(f"File too large ({size} bytes): {path}")
    return path.read_text(encoding="utf-8")


def load_data(path: Path | None) -> dict:
    if path is None:
        return {}
    raw = read_text(path, MAX_DATA_BYTES)
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RenderError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise RenderError("Data JSON must be an object (key/value pairs).")
    return sanitize_data(data)


def sanitize_data(data: dict[str, Any]) -> dict[str, str]:
    if len(data) > MAX_DATA_KEYS:
        raise RenderError(f"Data JSON has too many keys (max {MAX_DATA_KEYS})")

    sanitized: dict[str, str] = {}
    for raw_key, raw_value in data.items():
        if not isinstance(raw_key, str):
            raise RenderError("All JSON object keys must be strings")
        key = raw_key.strip()
        if not key:
            raise RenderError("Data keys must be non-empty")
        if len(key) > MAX_KEY_CHARS:
            raise RenderError(f"Data key exceeds {MAX_KEY_CHARS} characters: {raw_key!r}")
        if not PLACEHOLDER_KEY_PATTERN.fullmatch(key):
            raise RenderError(
                f"Unsupported placeholder key format: {raw_key!r} "
                "(expected letters/numbers/underscore and non-numeric start)"
            )

        if isinstance(raw_value, (dict, list, tuple, set)):
            raise RenderError(
                f"Value for key {raw_key!r} must be a scalar string/number/bool/null"
            )
        value = "" if raw_value is None else str(raw_value)
        if len(value) > MAX_VALUE_CHARS:
            raise RenderError(
                f"Value for key {raw_key!r} exceeds {MAX_VALUE_CHARS} characters"
            )
        sanitized[key] = html.escape(value, quote=False)
    return sanitized


def extract_placeholders(text: str) -> set[str]:
    placeholders: set[str] = set()
    for match in Template.pattern.finditer(text):
        name = match.group("named") or match.group("braced")
        if name:
            placeholders.add(name)
    return placeholders


def apply_template(template_text: str, data: dict[str, Any]) -> str:
    safe_data = sanitize_data(data)
    placeholders = extract_placeholders(template_text)
    merged = dict(safe_data)
    for key in placeholders:
        merged.setdefault(key, "")
    return Template(template_text).safe_substitute(merged)


def embed_css(html: str, css_text: str) -> str:
    style_block = f"<style>\n{css_text}\n</style>\n"
    if "</head>" in html:
        return html.replace("</head>", style_block + "</head>")
    return style_block + html


def find_engine(preferred: str) -> str | None:
    engines = ["wkhtmltopdf", "weasyprint", "pandoc"]
    if preferred != "auto":
        return preferred if shutil.which(preferred) else None
    for engine in engines:
        if shutil.which(engine):
            return engine
    return None


def _truncate(text: str, limit: int = MAX_COMMAND_ERROR_CHARS) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."


def run_command(cmd: list[str]) -> None:
    env = dict(os.environ)
    env.setdefault("LC_ALL", "C")
    env.setdefault("TZ", "UTC")
    try:
        subprocess.run(
            cmd,
            check=True,
            timeout=CONVERT_TIMEOUT_SEC,
            capture_output=True,
            text=True,
            env=env,
        )
    except subprocess.TimeoutExpired as exc:
        raise RenderError(f"PDF conversion timed out after {CONVERT_TIMEOUT_SEC}s") from exc
    except subprocess.CalledProcessError as exc:
        stderr = _truncate((exc.stderr or "").strip())
        raise RenderError(f"PDF conversion failed: {' '.join(cmd)}\n{stderr}") from exc


def validate_pdf_options(page_size: str, margin: str) -> tuple[str, str]:
    normalized_page_size = str(page_size).strip()
    normalized_margin = str(margin).strip()
    if not PAGE_SIZE_PATTERN.fullmatch(normalized_page_size):
        raise RenderError(
            "Invalid page size format; expected short token like A4/Letter/Legal"
        )
    if not MARGIN_PATTERN.fullmatch(normalized_margin):
        raise RenderError(
            "Invalid margin format; expected numeric unit like 14mm, 0.5in, or 12pt"
        )
    return normalized_page_size, normalized_margin


def convert_html_to_pdf(
    html_path: Path, pdf_path: Path, engine: str, page_size: str, margin: str
) -> None:
    if engine == "wkhtmltopdf":
        normalized_page_size, normalized_margin = validate_pdf_options(page_size, margin)
        cmd = [
            engine,
            "--disable-javascript",
            "--disable-local-file-access",
            "--page-size",
            normalized_page_size,
            "--margin-top",
            normalized_margin,
            "--margin-bottom",
            normalized_margin,
            "--margin-left",
            normalized_margin,
            "--margin-right",
            normalized_margin,
            str(html_path),
            str(pdf_path),
        ]
        run_command(cmd)
        return
    if engine == "weasyprint":
        cmd = [engine, str(html_path), str(pdf_path)]
        run_command(cmd)
        return
    if engine == "pandoc":
        cmd = [engine, str(html_path), "-o", str(pdf_path)]
        run_command(cmd)
        return
    raise RenderError(f"Unsupported engine: {engine}")


def render(args: argparse.Namespace) -> int:
    template_path = Path(args.template).resolve()
    output_path = Path(args.out).resolve()
    output_suffix = output_path.suffix.lower()
    if output_suffix not in {".html", ".htm", ".pdf"}:
        raise RenderError("Output must end with .html, .htm, or .pdf")

    template_text = read_text(template_path, MAX_TEMPLATE_BYTES)
    data = load_data(Path(args.data).resolve()) if args.data else {}
    rendered_html = apply_template(template_text, data)

    if args.css:
        css_text = read_text(Path(args.css).resolve(), MAX_CSS_BYTES)
        rendered_html = embed_css(rendered_html, css_text)
    if len(rendered_html.encode("utf-8")) > MAX_RENDERED_HTML_BYTES:
        raise RenderError(
            f"Rendered HTML exceeds {MAX_RENDERED_HTML_BYTES} bytes; reduce template/data size"
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)

    if output_suffix != ".pdf":
        output_path.write_text(rendered_html, encoding="utf-8")
        return 0

    page_size, margin = validate_pdf_options(args.page_size, args.margin)
    engine = find_engine(args.engine)
    if not engine:
        html_fallback = output_path.with_suffix(".html")
        html_fallback.write_text(rendered_html, encoding="utf-8")
        raise RenderError(
            "No PDF engine found. Install wkhtmltopdf, weasyprint, or pandoc. "
            f"HTML saved to {html_fallback}"
        )

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_html = Path(tmp_dir) / "render.html"
        tmp_html.write_text(rendered_html, encoding="utf-8")
        convert_html_to_pdf(
            tmp_html,
            output_path,
            engine,
            page_size=page_size,
            margin=margin,
        )

    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render ADHD templates to HTML or PDF")
    parser.add_argument("--template", required=True, help="Path to HTML template")
    parser.add_argument("--out", required=True, help="Output file (.html or .pdf)")
    parser.add_argument("--data", help="Optional JSON file with placeholder values")
    parser.add_argument(
        "--css",
        help="Optional CSS file to embed (use assets/styles/pdf.css)",
    )
    parser.add_argument(
        "--page-size",
        default=DEFAULT_PAGE_SIZE,
        help="Page size for PDF engines (default: A4)",
    )
    parser.add_argument(
        "--margin",
        default=DEFAULT_MARGIN,
        help="PDF margin for wkhtmltopdf (default: 14mm)",
    )
    parser.add_argument(
        "--engine",
        default="auto",
        choices=["auto", "wkhtmltopdf", "weasyprint", "pandoc"],
        help="PDF conversion engine",
    )
    return parser.parse_args()


def main() -> int:
    try:
        return render(parse_args())
    except RenderError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
