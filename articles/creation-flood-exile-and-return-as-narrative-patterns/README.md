# Creation, Flood, Exile, and Return as Narrative Patterns

This companion directory supports the article **Creation, Flood, Exile, and Return as Narrative Patterns**.

The scaffold treats creation, flood, exile, and return as auditable narrative-pattern functions rather than fixed universal formulas. It includes article-specific narrative-pattern diagnostics and the shared advanced Catalyst Canvas Python layer.

## What This Repository Adds

- Advanced additive `python/catalyst_canvas/` layer
- Article-specific `python/narrative_pattern_canvas/` layer
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
python3 python/run_creation_flood_exile_return_canvas_audit.py
python3 python/run_catalyst_canvas_audit.py --article-root .
Rscript r/run_all_creation_flood_exile_return_workflows.R
```

Outputs are written to:

```text
outputs/tables/
outputs/json/
outputs/markdown/
outputs/figures/
```
