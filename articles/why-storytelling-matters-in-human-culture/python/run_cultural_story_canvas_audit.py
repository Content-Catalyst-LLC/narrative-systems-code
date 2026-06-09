#!/usr/bin/env python3
"""Run the Cultural Story Canvas audit for Why Storytelling Matters in Human Culture."""

from __future__ import annotations

from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
PYTHON_ROOT = ARTICLE_ROOT / "python"

if str(PYTHON_ROOT) not in sys.path:
    sys.path.insert(0, str(PYTHON_ROOT))

from cultural_story_canvas.cli import run  # noqa: E402


if __name__ == "__main__":
    run(ARTICLE_ROOT)
