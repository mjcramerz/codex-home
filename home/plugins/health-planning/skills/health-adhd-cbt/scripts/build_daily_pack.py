#!/usr/bin/env python3
"""Convenience wrapper to render the full ADHD/CBT daily pack."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import render_template


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the ADHD/CBT daily template pack")
    parser.add_argument("--out", required=True, help="Output file (.html or .pdf)")
    parser.add_argument("--data", help="Optional JSON file with placeholder values")
    parser.add_argument(
        "--use-example",
        action="store_true",
        help="Use the included example data JSON",
    )
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
    output_path = Path(args.out).resolve()
    if output_path.suffix.lower() not in {".html", ".htm", ".pdf"}:
        print("ERROR: --out must end with .html, .htm, or .pdf", file=sys.stderr)
        return 2

    script_dir = Path(__file__).resolve().parent
    skill_dir = script_dir.parent
    assets_dir = skill_dir / "assets"

    template = assets_dir / "templates" / "daily-pack.html"
    css = assets_dir / "styles" / "pdf.css"
    example = assets_dir / "data" / "example.json"

    if args.use_example and args.data:
        print("ERROR: Use either --data or --use-example, not both.", file=sys.stderr)
        return 1

    data_path = args.data
    if args.use_example:
        data_path = str(example)

    namespace = argparse.Namespace(
        template=str(template),
        out=str(output_path),
        data=str(Path(data_path).resolve()) if data_path else None,
        css=str(css),
        engine=args.engine,
        page_size=args.page_size,
        margin=args.margin,
    )

    try:
        return render_template.render(namespace)
    except render_template.RenderError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
