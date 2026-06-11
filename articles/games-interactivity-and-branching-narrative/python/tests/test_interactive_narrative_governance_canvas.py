from __future__ import annotations

import unittest

from interactive_narrative_governance_canvas.models import InteractiveNarrativeGovernanceConfig, InteractiveNarrativeGovernanceRecord
from interactive_narrative_governance_canvas.validation import validate_record
from interactive_narrative_governance_canvas.scoring import agency_integrity, ai_interactive_narrative_risk, branching_burden, failure_and_identity_strength, governance_priority_score, review_priority, system_story_alignment


class InteractiveNarrativeGovernanceCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = InteractiveNarrativeGovernanceConfig()
        record = InteractiveNarrativeGovernanceRecord(
            "Test", "Context",
            0.8, 0.8, 0.7, 0.8, 0.7, 0.8,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.8, 0.8, 0.7, 0.7, 0.8, 0.8,
            0.8, 0.8, 0.7, 0.7,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.7,
            "editorial", "active", ""
        )
        validate_record(record, config)
        for value in [
            agency_integrity(record),
            branching_burden(record),
            system_story_alignment(record),
            failure_and_identity_strength(record),
            ai_interactive_narrative_risk(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
