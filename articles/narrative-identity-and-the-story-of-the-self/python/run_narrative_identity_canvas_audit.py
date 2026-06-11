#!/usr/bin/env python3
from pathlib import Path
import sys
ARTICLE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))
from narrative_identity_canvas.cli import main
if __name__ == "__main__": main()
