#!/usr/bin/env python3
"""Run the Story Media History Canvas audit for the storytelling history article."""

from __future__ import annotations

from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
PYTHON_ROOT = ARTICLE_ROOT / "python"

if str(PYTHON_ROOT) not in sys.path:
    sys.path.insert(0, str(PYTHON_ROOT))

from story_media_history_canvas.cli import run  # noqa: E402


if __name__ == "__main__":
    run(ARTICLE_ROOT)
