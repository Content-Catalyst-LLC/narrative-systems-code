#!/usr/bin/env bash
set -euo pipefail

ARTICLE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

python3 "${ARTICLE_ROOT}/python/run_public_story_governance_audit.py" --article-root "${ARTICLE_ROOT}"
python3 "${ARTICLE_ROOT}/python/run_catalyst_canvas_audit.py" --article-root "${ARTICLE_ROOT}" --strict

if command -v Rscript >/dev/null 2>&1; then
  Rscript "${ARTICLE_ROOT}/r/run_all_public_story_governance_workflows.R"
else
  echo "Rscript not found; skipping R smoke test."
fi

echo "Smoke tests complete."
