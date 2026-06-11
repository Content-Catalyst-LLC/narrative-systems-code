# Storytelling Across Oral, Literary, and Visual Media

This companion directory supports the article **Storytelling Across Oral, Literary, and Visual Media**.

The scaffold treats cross-media storytelling as a governance problem: oral, literary, visual, film, photographic, digital, archival, and AI-mediated stories are tested for medium-affordance fit, transfer risk, multimodal coherence, consent, provenance, context, and human review.

## What This Repository Adds

- Advanced additive `python/catalyst_canvas/` layer
- Article-specific `python/cross_media_story_governance_canvas/` layer
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
- Documentation and reusable cross-media story review templates

## Quick Start

```bash
python3 python/run_cross_media_story_governance_audit.py
python3 python/run_catalyst_canvas_audit.py --article-root .
Rscript r/run_all_cross_media_story_governance_workflows.R
```
