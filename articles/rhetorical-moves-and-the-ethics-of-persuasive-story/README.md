# Rhetorical Moves and the Ethics of Persuasive Story

This companion directory supports the article **Rhetorical Moves and the Ethics of Persuasive Story**.

The scaffold treats persuasive story as a governance problem: rhetorical integrity, manipulation risk, audience agency, evidence context, platform amplification, and AI persuasion risk are tested before publication.

## What This Repository Adds

- Advanced additive `python/catalyst_canvas/` layer
- Article-specific `python/rhetorical_moves_governance_canvas/` layer
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
- Documentation and reusable persuasive story review templates

## Quick Start

```bash
python3 python/run_rhetorical_moves_governance_audit.py
python3 python/run_catalyst_canvas_audit.py --article-root .
Rscript r/run_all_rhetorical_moves_governance_workflows.R
```
