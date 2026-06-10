from __future__ import annotations

import unittest

from meaning_architecture_canvas.models import MeaningArchitectureItem
from meaning_architecture_canvas.scoring import temporal_coherence, memory_durability, drift_risk, review_priority
from meaning_architecture_canvas.validation import validate_meaning_architecture_item


class MeaningArchitectureCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        item = MeaningArchitectureItem(
            "Test story",
            "test",
            0.8, 0.7, 0.6, 0.5, 0.8, 0.7,
            0.6, 0.7, 0.5, 0.6, 0.7,
            0.8, 0.2, 0.1, 0.6, 0.4, 0.9,
            "test-owner",
            "active",
        )
        validate_meaning_architecture_item(item)
        self.assertGreaterEqual(temporal_coherence(item), 0)
        self.assertLessEqual(temporal_coherence(item), 1)
        self.assertGreaterEqual(memory_durability(item), 0)
        self.assertLessEqual(memory_durability(item), 1)
        self.assertGreaterEqual(drift_risk(item), 0)
        self.assertLessEqual(drift_risk(item), 1)
        self.assertIn(review_priority(item), {"standard", "medium", "high"})

    def test_invalid_score_raises(self) -> None:
        item = MeaningArchitectureItem(
            "Bad story",
            "test",
            1.2, 0.7, 0.6, 0.5, 0.8, 0.7,
            0.6, 0.7, 0.5, 0.6, 0.7,
            0.8, 0.2, 0.1, 0.6, 0.4, 0.9,
            "test-owner",
            "active",
        )
        with self.assertRaises(ValueError):
            validate_meaning_architecture_item(item)


if __name__ == "__main__":
    unittest.main()
