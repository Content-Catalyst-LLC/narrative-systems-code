from __future__ import annotations

import unittest

from beginning_closure_canvas.models import BeginningClosureItem
from beginning_closure_canvas.scoring import (
    opening_clarity,
    closure_integrity,
    beginning_ending_alignment,
    closure_risk,
    governance_priority_score,
    review_priority,
)
from beginning_closure_canvas.validation import validate_beginning_closure_item


class BeginningClosureCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        item = BeginningClosureItem(
            "Test closure",
            "test",
            0.8, 0.7, 0.6, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.6, 0.7, 0.8, 0.7, 0.6,
            0.2, 0.3, 0.4, 0.3, 0.5,
            0.7, 0.6,
            "test-owner",
            "active",
        )
        validate_beginning_closure_item(item)
        self.assertGreaterEqual(opening_clarity(item), 0)
        self.assertLessEqual(opening_clarity(item), 1)
        self.assertGreaterEqual(closure_integrity(item), 0)
        self.assertLessEqual(closure_integrity(item), 1)
        self.assertGreaterEqual(beginning_ending_alignment(item), 0)
        self.assertLessEqual(beginning_ending_alignment(item), 1)
        self.assertGreaterEqual(closure_risk(item), 0)
        self.assertLessEqual(closure_risk(item), 1)
        self.assertGreaterEqual(governance_priority_score(item), 0)
        self.assertLessEqual(governance_priority_score(item), 1)
        self.assertIn(review_priority(item), {"standard", "medium", "high"})

    def test_invalid_score_raises(self) -> None:
        item = BeginningClosureItem(
            "Bad closure",
            "test",
            1.2, 0.7, 0.6, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.6, 0.7, 0.8, 0.7, 0.6,
            0.2, 0.3, 0.4, 0.3, 0.5,
            0.7, 0.6,
            "test-owner",
            "active",
        )
        with self.assertRaises(ValueError):
            validate_beginning_closure_item(item)


if __name__ == "__main__":
    unittest.main()
