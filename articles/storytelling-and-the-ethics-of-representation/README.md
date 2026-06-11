# Storytelling and the Ethics of Representation

This companion directory supports the article **Storytelling and the Ethics of Representation**.

The scaffold treats representation ethics as a governance problem: voice agency, context preservation, dignity, consent, source accuracy, power asymmetry, visual ethics, cultural protocols, testimony risk, institutional extraction, and AI-generated representation are tested for accountability before publication.

## What This Repository Adds

- Advanced additive `python/catalyst_canvas/` layer
- Article-specific `python/representation_ethics_governance_canvas/` layer
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
- Documentation and reusable representation review templates

## Quick Start

```bash
python3 python/run_representation_ethics_governance_audit.py
python3 python/run_catalyst_canvas_audit.py --article-root .
Rscript r/run_all_representation_ethics_governance_workflows.R
```
