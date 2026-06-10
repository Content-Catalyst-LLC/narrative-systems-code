from __future__ import annotations

import unittest

from narrative_understanding_canvas.models import NarrativeUnderstandingItem
from narrative_understanding_canvas.scoring import understanding_score, overreach_risk, review_priority
from narrative_understanding_canvas.validation import validate_narrative_understanding_item


class NarrativeUnderstandingCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        item = NarrativeUnderstandingItem(
            "Test story",
            "test",
            0.8, 0.7, 0.6, 0.5, 0.8, 0.7,
            0.6, 0.7, 0.5, 0.6,
            0.7, 0.8, 0.6,
            0.3, 0.4, 0.5, 0.4,
            "test-owner",
            "active",
        )
        validate_narrative_understanding_item(item)
        self.assertGreaterEqual(understanding_score(item), 0)
        self.assertLessEqual(understanding_score(item), 1)
        self.assertGreaterEqual(overreach_risk(item), 0)
        self.assertLessEqual(overreach_risk(item), 1)
        self.assertIn(review_priority(item), {"standard", "medium", "high"})

    def test_invalid_score_raises(self) -> None:
        item = NarrativeUnderstandingItem(
            "Bad story",
            "test",
            1.2, 0.7, 0.6, 0.5, 0.8, 0.7,
            0.6, 0.7, 0.5, 0.6,
            0.7, 0.8, 0.6,
            0.3, 0.4, 0.5, 0.4,
            "test-owner",
            "active",
        )
        with self.assertRaises(ValueError):
            validate_narrative_understanding_item(item)


if __name__ == "__main__":
    unittest.main()
