# Games, Interactivity, and Branching Narrative

This companion directory supports the article **Games, Interactivity, and Branching Narrative**.

The scaffold treats games and interactive narrative as a governance problem: player agency, branching burden, system-story alignment, consequence memory, failure design, identity care, multiplayer risk, procedural content, and AI-generated quest systems are tested for coherence, meaning, accessibility, and human review.

## What This Repository Adds

- Advanced additive `python/catalyst_canvas/` layer
- Article-specific `python/interactive_narrative_governance_canvas/` layer
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
- Documentation and reusable interactive narrative review templates

## Quick Start

```bash
python3 python/run_interactive_narrative_governance_audit.py
python3 python/run_catalyst_canvas_audit.py --article-root .
Rscript r/run_all_interactive_narrative_governance_workflows.R
```
