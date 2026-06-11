# Sacred History and Revelatory Narrative

This companion directory supports the article **Sacred History and Revelatory Narrative**.

The scaffold treats sacred-history and revelatory-narrative analysis as a governance-sensitive interpretive workflow. It includes article-specific sacred-history diagnostics and the shared advanced Catalyst Canvas Python layer.

## What This Repository Adds

- Advanced additive `python/catalyst_canvas/` layer
- Article-specific `python/sacred_history_canvas/` layer
- Typed dataclass models
- Config-driven scoring
- Validation
- Governance logic
- CSV, JSON, and markdown exporters
- CLI entrypoints
- Smoke tests
- Unit tests
- Canvas card generation
- Governance queue generation
- R diagnostics
- SQL schema and queries
- Documentation and reusable review templates

## Quick Start

```bash
python3 python/run_sacred_history_canvas_audit.py
python3 python/run_catalyst_canvas_audit.py --article-root .
Rscript r/run_all_sacred_history_workflows.R
```

Outputs are written to:

```text
outputs/tables/
outputs/json/
outputs/markdown/
outputs/figures/
```
