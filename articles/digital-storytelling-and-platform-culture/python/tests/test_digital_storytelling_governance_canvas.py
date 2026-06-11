from __future__ import annotations

import unittest

from digital_storytelling_governance_canvas.models import DigitalStorytellingGovernanceConfig, DigitalStorytellingGovernanceRecord
from digital_storytelling_governance_canvas.validation import validate_record
from digital_storytelling_governance_canvas.scoring import ai_synthetic_story_risk, archive_memory_strength, context_collapse_risk, governance_priority_score, platform_formula_drift, platform_narrative_integrity, review_priority


class DigitalStorytellingGovernanceCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = DigitalStorytellingGovernanceConfig()
        record = DigitalStorytellingGovernanceRecord(
            "Test", "Context",
            0.8, 0.8, 0.7, 0.8, 0.7, 0.8,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.8, 0.8, 0.7, 0.7,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.7,
            "editorial", "active", ""
        )
        validate_record(record, config)
        for value in [
            platform_narrative_integrity(record),
            context_collapse_risk(record),
            platform_formula_drift(record),
            archive_memory_strength(record),
            ai_synthetic_story_risk(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
