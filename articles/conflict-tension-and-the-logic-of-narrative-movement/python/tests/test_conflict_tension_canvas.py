from __future__ import annotations

import unittest

from conflict_tension_canvas.models import ConflictTensionItem
from conflict_tension_canvas.scoring import (
    conflict_clarity,
    tension_durability,
    narrative_movement,
    conflict_risk,
    governance_priority_score,
    review_priority,
)
from conflict_tension_canvas.validation import validate_conflict_tension_item


class ConflictTensionCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        item = ConflictTensionItem(
            "Test conflict",
            "test",
            0.8, 0.7, 0.6, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.6, 0.5, 0.7,
            0.6, 0.7, 0.5, 0.6, 0.7, 0.8,
            0.2, 0.3, 0.4, 0.3, 0.5,
            0.7, 0.6,
            "test-owner",
            "active",
        )
        validate_conflict_tension_item(item)
        self.assertGreaterEqual(conflict_clarity(item), 0)
        self.assertLessEqual(conflict_clarity(item), 1)
        self.assertGreaterEqual(tension_durability(item), 0)
        self.assertLessEqual(tension_durability(item), 1)
        self.assertGreaterEqual(narrative_movement(item), 0)
        self.assertLessEqual(narrative_movement(item), 1)
        self.assertGreaterEqual(conflict_risk(item), 0)
        self.assertLessEqual(conflict_risk(item), 1)
        self.assertGreaterEqual(governance_priority_score(item), 0)
        self.assertLessEqual(governance_priority_score(item), 1)
        self.assertIn(review_priority(item), {"standard", "medium", "high"})

    def test_invalid_score_raises(self) -> None:
        item = ConflictTensionItem(
            "Bad conflict",
            "test",
            1.2, 0.7, 0.6, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.6, 0.5, 0.7,
            0.6, 0.7, 0.5, 0.6, 0.7, 0.8,
            0.2, 0.3, 0.4, 0.3, 0.5,
            0.7, 0.6,
            "test-owner",
            "active",
        )
        with self.assertRaises(ValueError):
            validate_conflict_tension_item(item)


if __name__ == "__main__":
    unittest.main()
