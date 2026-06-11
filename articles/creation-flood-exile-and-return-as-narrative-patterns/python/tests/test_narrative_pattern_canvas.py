from __future__ import annotations

import unittest

from narrative_pattern_canvas.models import NarrativePatternRecord, PatternConfig
from narrative_pattern_canvas.validation import validate_record
from narrative_pattern_canvas.scoring import (
    ethical_risk,
    governance_priority_score,
    interpretation_readiness,
    pattern_strength,
    review_priority,
    rupture_renewal_strength,
)


class NarrativePatternCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = PatternConfig()
        record = NarrativePatternRecord(
            "Test",
            "Context",
            0.8, 0.7, 0.6, 0.7,
            0.8, 0.8,
            0.8, 0.7, 0.7, 0.8, 0.7, 0.8,
            0.3, 0.4, 0.3, 0.4, 0.4,
            0.7,
            "editorial",
            "active",
            "",
        )
        validate_record(record, config)
        for value in [
            pattern_strength(record),
            rupture_renewal_strength(record),
            ethical_risk(record),
            interpretation_readiness(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
