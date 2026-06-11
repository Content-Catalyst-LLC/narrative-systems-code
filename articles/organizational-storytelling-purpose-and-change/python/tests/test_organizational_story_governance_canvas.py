from __future__ import annotations

import unittest

from organizational_story_governance_canvas.models import OrganizationalStoryGovernanceConfig, OrganizationalStoryGovernanceRecord
from organizational_story_governance_canvas.validation import validate_record
from organizational_story_governance_canvas.scoring import ai_organizational_story_risk, change_credibility, employee_voice_integrity, governance_priority_score, narrative_extraction_risk, organizational_memory_strength, purpose_alignment, review_priority


class OrganizationalStoryGovernanceCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = OrganizationalStoryGovernanceConfig()
        record = OrganizationalStoryGovernanceRecord(
            "Test", "Context",
            0.8, 0.8, 0.7, 0.7, 0.8, 0.7,
            0.8, 0.7, 0.8, 0.7, 0.8, 0.7,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.8, 0.8, 0.8, 0.7,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.7,
            "editorial", "active", ""
        )
        validate_record(record, config)
        for value in [
            purpose_alignment(record),
            change_credibility(record),
            narrative_extraction_risk(record),
            employee_voice_integrity(record),
            organizational_memory_strength(record),
            ai_organizational_story_risk(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
