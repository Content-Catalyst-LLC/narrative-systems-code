from __future__ import annotations

import unittest

from rhetorical_moves_governance_canvas.models import RhetoricalMovesGovernanceConfig, RhetoricalMovesGovernanceRecord
from rhetorical_moves_governance_canvas.validation import validate_record
from rhetorical_moves_governance_canvas.scoring import ai_persuasion_risk, audience_agency_score, governance_priority_score, manipulation_risk, platform_persuasion_risk, rhetorical_integrity, review_priority


class RhetoricalMovesGovernanceCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = RhetoricalMovesGovernanceConfig()
        record = RhetoricalMovesGovernanceRecord(
            "Test", "Context",
            0.8, 0.8, 0.7, 0.8, 0.7, 0.8,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.8, 0.7, 0.7, 0.8, 0.7, 0.7,
            0.3, 0.4, 0.3, 0.8,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.7,
            "editorial", "active", ""
        )
        validate_record(record, config)
        for value in [
            rhetorical_integrity(record),
            manipulation_risk(record),
            audience_agency_score(record),
            platform_persuasion_risk(record),
            ai_persuasion_risk(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
