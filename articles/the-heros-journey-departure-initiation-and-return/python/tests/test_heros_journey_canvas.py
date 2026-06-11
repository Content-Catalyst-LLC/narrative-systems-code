from __future__ import annotations

import unittest

from heros_journey_canvas.scoring import (
    HerosJourneyClaim,
    journey_structure,
    formula_drift,
    interpretation_readiness,
    governance_priority_score,
    review_priority,
)


class HerosJourneyCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        claim = HerosJourneyClaim(
            "Test",
            "Context",
            0.8, 0.7, 0.6, 0.8, 0.7, 0.6,
            0.7, 0.6, 0.7,
            0.2, 0.3, 0.4, 0.3, 0.5, 0.7,
            0.7, 0.6, 0.8, 0.7, 0.6,
            "owner",
            "active",
        )
        for value in [
            journey_structure(claim),
            formula_drift(claim),
            interpretation_readiness(claim),
            governance_priority_score(claim),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(claim), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
