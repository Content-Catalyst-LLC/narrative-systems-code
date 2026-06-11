from __future__ import annotations

import unittest

from compact_oral_forms_canvas.models import CompactOralFormItem
from compact_oral_forms_canvas.scoring import (
    oral_form_context,
    sound_and_repetition,
    ritual_authority,
    archive_risk,
    governance_priority_score,
    review_priority,
)
from compact_oral_forms_canvas.validation import validate_compact_oral_form_item


class CompactOralFormsCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        item = CompactOralFormItem(
            "Test oral form",
            "proverb",
            0.8, 0.7, 0.6, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.2, 0.3, 0.4, 0.3, 0.5, 0.7,
            0.7, 0.6,
            "test-owner",
            "active",
        )
        validate_compact_oral_form_item(item)
        self.assertGreaterEqual(oral_form_context(item), 0)
        self.assertLessEqual(oral_form_context(item), 1)
        self.assertGreaterEqual(sound_and_repetition(item), 0)
        self.assertLessEqual(sound_and_repetition(item), 1)
        self.assertGreaterEqual(ritual_authority(item), 0)
        self.assertLessEqual(ritual_authority(item), 1)
        self.assertGreaterEqual(archive_risk(item), 0)
        self.assertLessEqual(archive_risk(item), 1)
        self.assertGreaterEqual(governance_priority_score(item), 0)
        self.assertLessEqual(governance_priority_score(item), 1)
        self.assertIn(review_priority(item), {"standard", "medium", "high"})

    def test_invalid_score_raises(self) -> None:
        item = CompactOralFormItem(
            "Bad oral form",
            "chant",
            1.2, 0.7, 0.6, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.2, 0.3, 0.4, 0.3, 0.5, 0.7,
            0.7, 0.6,
            "test-owner",
            "active",
        )
        with self.assertRaises(ValueError):
            validate_compact_oral_form_item(item)


if __name__ == "__main__":
    unittest.main()
