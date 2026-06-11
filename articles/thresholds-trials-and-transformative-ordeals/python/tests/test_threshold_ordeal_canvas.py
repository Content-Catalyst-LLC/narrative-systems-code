from __future__ import annotations

import unittest

from threshold_ordeal_canvas.scoring import (
    ThresholdOrdealClaim,
    ethical_risk,
    interpretation_readiness,
    governance_priority_score,
    review_priority,
)


class ThresholdOrdealCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        claim = ThresholdOrdealClaim(
            "Test",
            "Context",
            0.8, 0.7, 0.6,
            0.2, 0.3, 0.4, 0.3, 0.5, 0.7,
            0.7, 0.6, 0.8, 0.7, 0.6,
            0.7, 0.6,
            "owner",
            "active",
        )
        for value in [
            ethical_risk(claim),
            interpretation_readiness(claim),
            governance_priority_score(claim),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(claim), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
