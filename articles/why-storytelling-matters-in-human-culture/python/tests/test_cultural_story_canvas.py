from __future__ import annotations

import unittest

from cultural_story_canvas.models import CulturalStoryItem
from cultural_story_canvas.scoring import cultural_value_score, narrative_risk, review_priority
from cultural_story_canvas.validation import validate_cultural_story_item


class CulturalStoryCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        item = CulturalStoryItem(
            "Test cultural story",
            "test",
            "A contextualized cultural story used for testing.",
            0.8, 0.7, 0.6, 0.5, 0.9, 0.4, 0.8,
            0.7, 0.6, 0.5, 0.6, 0.7,
            "test-owner",
            "active",
        )
        validate_cultural_story_item(item)
        self.assertGreaterEqual(cultural_value_score(item), 0)
        self.assertLessEqual(cultural_value_score(item), 1)
        self.assertGreaterEqual(narrative_risk(item), 0)
        self.assertLessEqual(narrative_risk(item), 1)
        self.assertIn(review_priority(item), {"standard", "medium", "high"})

    def test_invalid_score_raises(self) -> None:
        item = CulturalStoryItem(
            "Bad cultural story",
            "test",
            "A contextualized cultural story used for testing.",
            1.2, 0.7, 0.6, 0.5, 0.9, 0.4, 0.8,
            0.7, 0.6, 0.5, 0.6, 0.7,
            "test-owner",
            "active",
        )
        with self.assertRaises(ValueError):
            validate_cultural_story_item(item)


if __name__ == "__main__":
    unittest.main()
