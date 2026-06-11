from __future__ import annotations

import unittest

from postcolonial_narrative_form_canvas.models import PostcolonialNarrativeFormConfig, PostcolonialNarrativeFormRecord
from postcolonial_narrative_form_canvas.validation import validate_record
from postcolonial_narrative_form_canvas.scoring import colonial_form_risk, digital_coloniality, governance_priority_score, postcolonial_form_strength, review_priority, translation_governance


class PostcolonialNarrativeFormCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = PostcolonialNarrativeFormConfig()
        record = PostcolonialNarrativeFormRecord(
            "Test",
            "Context",
            0.5, 0.6, 0.5, 0.6, 0.5, 0.8,
            0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8,
            0.8, 0.8, 0.8, 0.8, 0.8, 0.8,
            0.6, 0.5, 0.5, 0.5, 0.4, 0.8,
            0.7,
            "editorial",
            "active",
            "",
        )
        validate_record(record, config)
        for value in [
            colonial_form_risk(record),
            postcolonial_form_strength(record),
            translation_governance(record),
            digital_coloniality(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
