from __future__ import annotations

import os
import subprocess
import sys


def test_help() -> None:
    p = subprocess.run([sys.executable, "-m", "cli_app", "--help"], capture_output=True, text=True)
    assert p.returncode == 0
    assert "Python CLI template" in p.stdout


def test_version() -> None:
    p = subprocess.run([sys.executable, "-m", "cli_app", "--version"], capture_output=True, text=True)
    assert p.returncode == 0
    assert "0.1.0" in p.stdout


def test_log_format_env() -> None:
    env = dict(os.environ)
    env["LOG_FORMAT"] = "json"
    p = subprocess.run([sys.executable, "-m", "cli_app"], capture_output=True, text=True, env=env)
    assert p.returncode == 0
    assert p.stderr.strip().startswith("{")
