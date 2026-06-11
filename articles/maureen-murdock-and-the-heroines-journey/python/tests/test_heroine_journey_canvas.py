from __future__ import annotations

import unittest

from heroine_journey_canvas.models import HeroineJourneyConfig, HeroineJourneyRecord
from heroine_journey_canvas.validation import validate_record
from heroine_journey_canvas.scoring import critique_readiness, framework_risk, governance_priority_score, heroine_alignment, integration_quality, review_priority


class HeroineJourneyCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = HeroineJourneyConfig()
        record = HeroineJourneyRecord(
            "Test",
            "Context",
            0.8, 0.8, 0.7, 0.8, 0.8, 0.7,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.8, 0.8, 0.8, 0.8, 0.8,
            0.8, 0.8, 0.8, 0.8, 0.8, 0.8,
            0.7,
            "editorial",
            "active",
            "",
        )
        validate_record(record, config)
        for value in [
            heroine_alignment(record),
            framework_risk(record),
            critique_readiness(record),
            integration_quality(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
