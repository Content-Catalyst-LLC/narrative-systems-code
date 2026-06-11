# Adaptation and the Migration of Stories Across Media

This companion directory supports the article **Adaptation and the Migration of Stories Across Media**.

The scaffold treats adaptation as governed transformation across media, audiences, institutions, rights regimes, memory systems, platforms, franchises, and AI-mediated workflows. It audits source-core preservation, medium fit, transfer loss, franchise drift, consent, provenance, context preservation, and AI adaptation risk.

## What This Repository Adds

- Advanced additive `python/catalyst_canvas/` layer
- Article-specific `python/adaptation_governance_canvas/` layer
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
- Documentation and reusable adaptation review templates

## Quick Start

```bash
python3 python/run_adaptation_governance_audit.py
python3 python/run_catalyst_canvas_audit.py --article-root .
Rscript r/run_all_adaptation_governance_workflows.R
```
