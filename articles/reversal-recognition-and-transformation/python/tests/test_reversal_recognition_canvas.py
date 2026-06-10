from __future__ import annotations

import unittest

from reversal_recognition_canvas.models import ReversalRecognitionItem
from reversal_recognition_canvas.scoring import (
    reversal_integrity,
    recognition_clarity,
    transformation_depth,
    recognition_risk,
    governance_priority_score,
    review_priority,
)
from reversal_recognition_canvas.validation import validate_reversal_recognition_item


class ReversalRecognitionCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        item = ReversalRecognitionItem(
            "Test recognition",
            "test",
            0.8, 0.7, 0.6, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.6, 0.5, 0.7,
            0.6, 0.7, 0.5, 0.6, 0.7, 0.8,
            0.2, 0.3, 0.4, 0.3,
            0.7, 0.6,
            "test-owner",
            "active",
        )
        validate_reversal_recognition_item(item)
        self.assertGreaterEqual(reversal_integrity(item), 0)
        self.assertLessEqual(reversal_integrity(item), 1)
        self.assertGreaterEqual(recognition_clarity(item), 0)
        self.assertLessEqual(recognition_clarity(item), 1)
        self.assertGreaterEqual(transformation_depth(item), 0)
        self.assertLessEqual(transformation_depth(item), 1)
        self.assertGreaterEqual(recognition_risk(item), 0)
        self.assertLessEqual(recognition_risk(item), 1)
        self.assertGreaterEqual(governance_priority_score(item), 0)
        self.assertLessEqual(governance_priority_score(item), 1)
        self.assertIn(review_priority(item), {"standard", "medium", "high"})

    def test_invalid_score_raises(self) -> None:
        item = ReversalRecognitionItem(
            "Bad recognition",
            "test",
            1.2, 0.7, 0.6, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.6, 0.5, 0.7,
            0.6, 0.7, 0.5, 0.6, 0.7, 0.8,
            0.2, 0.3, 0.4, 0.3,
            0.7, 0.6,
            "test-owner",
            "active",
        )
        with self.assertRaises(ValueError):
            validate_reversal_recognition_item(item)


if __name__ == "__main__":
    unittest.main()
