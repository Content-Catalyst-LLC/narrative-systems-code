from __future__ import annotations

import unittest

from indigenous_story_governance_canvas.models import IndigenousStoryGovernanceConfig, IndigenousStoryGovernanceRecord
from indigenous_story_governance_canvas.validation import validate_record
from indigenous_story_governance_canvas.scoring import digital_sovereignty_risk, governance_priority_score, place_memory_strength, protocol_risk, relational_accountability, review_priority, translation_governance


class IndigenousStoryGovernanceCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = IndigenousStoryGovernanceConfig()
        record = IndigenousStoryGovernanceRecord(
            "Test",
            "Context",
            0.8, 0.8, 0.7, 0.7, 0.8, 0.8,
            0.4, 0.3, 0.3, 0.4, 0.5,
            0.8, 0.8, 0.8, 0.8, 0.7, 0.8,
            0.8, 0.8, 0.8, 0.7, 0.8, 0.8,
            0.4, 0.5, 0.5, 0.4, 0.4, 0.8,
            0.7,
            "editorial",
            "active",
            "",
        )
        validate_record(record, config)
        for value in [
            relational_accountability(record),
            protocol_risk(record),
            place_memory_strength(record),
            translation_governance(record),
            digital_sovereignty_risk(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
