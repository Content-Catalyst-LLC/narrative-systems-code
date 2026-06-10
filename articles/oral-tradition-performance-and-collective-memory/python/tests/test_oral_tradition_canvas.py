from __future__ import annotations

import unittest

from oral_tradition_canvas.models import OralTraditionItem
from oral_tradition_canvas.scoring import (
    performance_context,
    transmission_integrity,
    memory_function,
    archive_risk,
    governance_priority_score,
    review_priority,
)
from oral_tradition_canvas.validation import validate_oral_tradition_item


class OralTraditionCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        item = OralTraditionItem(
            "Test oral tradition",
            "test",
            0.8, 0.7, 0.6, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.2, 0.3, 0.4, 0.3, 0.5, 0.7,
            0.7, 0.6,
            "test-owner",
            "active",
        )
        validate_oral_tradition_item(item)
        self.assertGreaterEqual(performance_context(item), 0)
        self.assertLessEqual(performance_context(item), 1)
        self.assertGreaterEqual(transmission_integrity(item), 0)
        self.assertLessEqual(transmission_integrity(item), 1)
        self.assertGreaterEqual(memory_function(item), 0)
        self.assertLessEqual(memory_function(item), 1)
        self.assertGreaterEqual(archive_risk(item), 0)
        self.assertLessEqual(archive_risk(item), 1)
        self.assertGreaterEqual(governance_priority_score(item), 0)
        self.assertLessEqual(governance_priority_score(item), 1)
        self.assertIn(review_priority(item), {"standard", "medium", "high"})

    def test_invalid_score_raises(self) -> None:
        item = OralTraditionItem(
            "Bad oral tradition",
            "test",
            1.2, 0.7, 0.6, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.2, 0.3, 0.4, 0.3, 0.5, 0.7,
            0.7, 0.6,
            "test-owner",
            "active",
        )
        with self.assertRaises(ValueError):
            validate_oral_tradition_item(item)


if __name__ == "__main__":
    unittest.main()
