from __future__ import annotations

import unittest

from comparative_myth_canvas.models import ComparativeMythClaim
from comparative_myth_canvas.scoring import (
    comparative_pattern,
    cultural_specificity,
    generalization_risk,
    interpretation_readiness,
    governance_priority_score,
    review_priority,
)
from comparative_myth_canvas.validation import validate_comparative_myth_claim


class ComparativeMythCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        claim = ComparativeMythClaim(
            "Test myth claim",
            "test context",
            0.8, 0.7, 0.6, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.2, 0.3, 0.4, 0.3, 0.5, 0.7,
            0.7, 0.6, 0.7, 0.8,
            0.7, 0.6,
            "test-owner",
            "active",
        )
        validate_comparative_myth_claim(claim)
        self.assertGreaterEqual(comparative_pattern(claim), 0)
        self.assertLessEqual(comparative_pattern(claim), 1)
        self.assertGreaterEqual(cultural_specificity(claim), 0)
        self.assertLessEqual(cultural_specificity(claim), 1)
        self.assertGreaterEqual(generalization_risk(claim), 0)
        self.assertLessEqual(generalization_risk(claim), 1)
        self.assertGreaterEqual(interpretation_readiness(claim), 0)
        self.assertLessEqual(interpretation_readiness(claim), 1)
        self.assertGreaterEqual(governance_priority_score(claim), 0)
        self.assertLessEqual(governance_priority_score(claim), 1)
        self.assertIn(review_priority(claim), {"standard", "medium", "high"})

    def test_invalid_score_raises(self) -> None:
        claim = ComparativeMythClaim(
            "Bad myth claim",
            "test context",
            1.2, 0.7, 0.6, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.2, 0.3, 0.4, 0.3, 0.5, 0.7,
            0.7, 0.6, 0.7, 0.8,
            0.7, 0.6,
            "test-owner",
            "active",
        )
        with self.assertRaises(ValueError):
            validate_comparative_myth_claim(claim)


if __name__ == "__main__":
    unittest.main()
