# Narratology and the Grammar of Story

This companion directory supports the article **Narratology and the Grammar of Story**.

The scaffold treats narratology as an auditable narrative-grammar workflow. It includes article-specific diagnostics for story/discourse, voice, focalization, temporal structure, narrative levels, reliability, information control, character agency, and ethical risk, plus the shared advanced Catalyst Canvas Python layer.

## What This Repository Adds

- Advanced additive `python/catalyst_canvas/` layer
- Article-specific `python/narratology_canvas/` layer
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
python3 python/run_narratology_canvas_audit.py
python3 python/run_catalyst_canvas_audit.py --article-root .
Rscript r/run_all_narratology_workflows.R
```
