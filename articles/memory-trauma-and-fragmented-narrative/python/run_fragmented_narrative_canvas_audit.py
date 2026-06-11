#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
PYTHON_ROOT = ARTICLE_ROOT / "python"

if str(PYTHON_ROOT) not in sys.path:
    sys.path.insert(0, str(PYTHON_ROOT))

from fragmented_narrative_canvas.cli import main  # noqa: E402

if __name__ == "__main__":
    main()
