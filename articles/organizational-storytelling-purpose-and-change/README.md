# Organizational Storytelling, Purpose, and Change

This companion directory supports the article **Organizational Storytelling, Purpose, and Change**.

The scaffold treats organizational storytelling as a governance problem: purpose stories, change narratives, employee voice, stakeholder impact, institutional memory, and AI-generated culture summaries are tested against evidence, participation, agency, dissent visibility, and actual practice.

## What This Repository Adds

- Advanced additive `python/catalyst_canvas/` layer
- Article-specific `python/organizational_story_governance_canvas/` layer
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
- Documentation and reusable purpose-and-change review templates

## Quick Start

```bash
python3 python/run_organizational_story_governance_audit.py
python3 python/run_catalyst_canvas_audit.py --article-root .
Rscript r/run_all_organizational_story_governance_workflows.R
```
