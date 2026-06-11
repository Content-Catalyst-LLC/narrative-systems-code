# Serial Storytelling, Television, and Long-Form Narrative

This companion directory supports the article **Serial Storytelling, Television, and Long-Form Narrative**.

The scaffold treats serial television and long-form narrative as a governance problem: episodes, season arcs, continuity, ensemble balance, payoff integrity, audience memory, ending accountability, platform time, and AI-generated season planning are tested for coherence, risk, accessibility, and human review.

## What This Repository Adds

- Advanced additive `python/catalyst_canvas/` layer
- Article-specific `python/serial_narrative_governance_canvas/` layer
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
- Documentation and reusable serial narrative review templates

## Quick Start

```bash
python3 python/run_serial_narrative_governance_audit.py
python3 python/run_catalyst_canvas_audit.py --article-root .
Rscript r/run_all_serial_narrative_governance_workflows.R
```
