from __future__ import annotations

import unittest

from monomyth_canvas.models import MonomythClaim
from monomyth_canvas.scoring import (
    monomyth_pattern,
    specificity_preservation,
    formula_drift,
    interpretation_readiness,
    governance_priority_score,
    review_priority,
)
from monomyth_canvas.validation import validate_monomyth_claim


class MonomythCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        claim = MonomythClaim(
            "Test monomyth claim",
            "test context",
            0.8, 0.7, 0.6, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.2, 0.3, 0.4, 0.3, 0.5, 0.7,
            0.7, 0.6, 0.7, 0.8,
            0.7, 0.6,
            "test-owner",
            "active",
        )
        validate_monomyth_claim(claim)
        self.assertGreaterEqual(monomyth_pattern(claim), 0)
        self.assertLessEqual(monomyth_pattern(claim), 1)
        self.assertGreaterEqual(specificity_preservation(claim), 0)
        self.assertLessEqual(specificity_preservation(claim), 1)
        self.assertGreaterEqual(formula_drift(claim), 0)
        self.assertLessEqual(formula_drift(claim), 1)
        self.assertGreaterEqual(interpretation_readiness(claim), 0)
        self.assertLessEqual(interpretation_readiness(claim), 1)
        self.assertGreaterEqual(governance_priority_score(claim), 0)
        self.assertLessEqual(governance_priority_score(claim), 1)
        self.assertIn(review_priority(claim), {"standard", "medium", "high"})

    def test_invalid_score_raises(self) -> None:
        claim = MonomythClaim(
            "Bad monomyth claim",
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
            validate_monomyth_claim(claim)


if __name__ == "__main__":
    unittest.main()
