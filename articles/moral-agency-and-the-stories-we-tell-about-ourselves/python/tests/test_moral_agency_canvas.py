from __future__ import annotations

import unittest

from moral_agency_canvas.models import MoralAgencyConfig, MoralAgencyRecord
from moral_agency_canvas.validation import validate_record
from moral_agency_canvas.scoring import excuse_risk, governance_priority_score, interpretation_readiness, moral_clarity, repair_readiness, review_priority


class MoralAgencyCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = MoralAgencyConfig()
        record = MoralAgencyRecord(
            "Test",
            "Context",
            0.8, 0.8, 0.7, 0.8, 0.8, 0.7,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.4,
            0.8, 0.7, 0.8, 0.8, 0.7, 0.8,
            0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.7,
            "editorial",
            "active",
            "",
        )
        validate_record(record, config)
        for value in [
            moral_clarity(record),
            excuse_risk(record),
            repair_readiness(record),
            interpretation_readiness(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
