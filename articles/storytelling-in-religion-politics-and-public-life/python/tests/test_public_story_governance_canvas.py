from __future__ import annotations

import unittest

from public_story_governance_canvas.models import PublicStoryGovernanceConfig, PublicStoryGovernanceRecord
from public_story_governance_canvas.validation import validate_record
from public_story_governance_canvas.scoring import ai_public_rhetoric_risk, civil_religion_accountability, governance_priority_score, mythic_simplification_risk, public_narrative_strength, review_priority, testimony_ethics


class PublicStoryGovernanceCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = PublicStoryGovernanceConfig()
        record = PublicStoryGovernanceRecord(
            "Test",
            "Context",
            0.8, 0.8, 0.7, 0.7, 0.8, 0.8,
            0.4, 0.4, 0.5, 0.5, 0.3, 0.8,
            0.8, 0.8, 0.7, 0.8, 0.7, 0.7,
            0.8, 0.8, 0.8, 0.7,
            0.4, 0.5, 0.4, 0.4, 0.4, 0.8,
            0.7,
            "editorial",
            "active",
            "",
        )
        validate_record(record, config)
        for value in [
            public_narrative_strength(record),
            mythic_simplification_risk(record),
            civil_religion_accountability(record),
            testimony_ethics(record),
            ai_public_rhetoric_risk(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
