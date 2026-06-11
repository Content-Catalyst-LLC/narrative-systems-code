from __future__ import annotations

import unittest

from four_function_myth_canvas.scoring import (
    MythFunctionClaim,
    function_balance,
    cultural_work,
    sociological_risk,
    interpretation_readiness,
    governance_priority_score,
    review_priority,
)


class FourFunctionMythCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        claim = MythFunctionClaim(
            "Test",
            "Context",
            0.7, 0.8, 0.6, 0.9, 0.7, 0.6,
            0.2, 0.3, 0.4, 0.3, 0.5, 0.7,
            0.7, 0.6, 0.8, 0.7, 0.6,
            0.7, 0.6,
            "owner",
            "active",
        )
        for value in [
            function_balance(claim),
            cultural_work(claim),
            sociological_risk(claim),
            interpretation_readiness(claim),
            governance_priority_score(claim),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(claim), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
