from __future__ import annotations

import argparse
import logging
import os
import sys

from . import __version__
from .logging_ import configure_logging

log = logging.getLogger("cli_app")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="cli_app", description="Python CLI template")
    p.add_argument("-v", "--verbose", action="count", default=0, help="Increase verbosity (-v, -vv)")
    default_log_format = os.getenv("LOG_FORMAT", "text").lower()
    if default_log_format not in {"text", "json"}:
        default_log_format = "text"
    p.add_argument("--log-format", choices=["text", "json"], default=default_log_format)
    p.add_argument("--version", action="version", version=__version__)
    return p


def main(argv: list[str]) -> int:
    args = build_parser().parse_args(argv)

    default_level = os.getenv("LOG_LEVEL", "INFO").upper()
    level = "DEBUG" if args.verbose >= 1 else default_level
    configure_logging(level=level, log_format=args.log_format)

    log.info("starting")
    print("ok", file=sys.stdout)
    return 0


def main_cli() -> int:
    return main(sys.argv[1:])


if __name__ == "__main__":
    raise SystemExit(main_cli())
