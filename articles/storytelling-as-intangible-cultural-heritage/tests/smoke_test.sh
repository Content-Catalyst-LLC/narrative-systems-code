#!/usr/bin/env bash
set -euo pipefail

ARTICLE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

python3 "${ARTICLE_ROOT}/python/run_storytelling_heritage_canvas_audit.py"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "${ARTICLE_ROOT}/r/run_all_storytelling_heritage_workflows.R"
else
  echo "Rscript not found; skipping R smoke test."
fi

echo "Smoke tests complete."
