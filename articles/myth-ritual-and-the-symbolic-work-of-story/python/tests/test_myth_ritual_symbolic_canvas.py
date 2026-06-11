from __future__ import annotations

import unittest

from myth_ritual_symbolic_canvas.models import MythRitualSymbolicItem
from myth_ritual_symbolic_canvas.scoring import (
    symbolic_function,
    ritual_context,
    ethical_risk,
    interpretation_readiness,
    governance_priority_score,
    review_priority,
)
from myth_ritual_symbolic_canvas.validation import validate_myth_ritual_symbolic_item


class MythRitualSymbolicCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        item = MythRitualSymbolicItem(
            "Test myth ritual item",
            "test context",
            0.8, 0.7, 0.6, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.2, 0.3, 0.4, 0.3, 0.5, 0.7,
            0.7, 0.6, 0.7, 0.8, 0.7, 0.6,
            0.7, 0.6,
            "test-owner",
            "active",
        )
        validate_myth_ritual_symbolic_item(item)
        self.assertGreaterEqual(symbolic_function(item), 0)
        self.assertLessEqual(symbolic_function(item), 1)
        self.assertGreaterEqual(ritual_context(item), 0)
        self.assertLessEqual(ritual_context(item), 1)
        self.assertGreaterEqual(ethical_risk(item), 0)
        self.assertLessEqual(ethical_risk(item), 1)
        self.assertGreaterEqual(interpretation_readiness(item), 0)
        self.assertLessEqual(interpretation_readiness(item), 1)
        self.assertGreaterEqual(governance_priority_score(item), 0)
        self.assertLessEqual(governance_priority_score(item), 1)
        self.assertIn(review_priority(item), {"standard", "medium", "high"})

    def test_invalid_score_raises(self) -> None:
        item = MythRitualSymbolicItem(
            "Bad myth ritual item",
            "test context",
            1.2, 0.7, 0.6, 0.8, 0.7, 0.6,
            0.6, 0.7, 0.8, 0.7, 0.6, 0.7,
            0.2, 0.3, 0.4, 0.3, 0.5, 0.7,
            0.7, 0.6, 0.7, 0.8, 0.7, 0.6,
            0.7, 0.6,
            "test-owner",
            "active",
        )
        with self.assertRaises(ValueError):
            validate_myth_ritual_symbolic_item(item)


if __name__ == "__main__":
    unittest.main()
