from __future__ import annotations

import unittest

from fragmented_narrative_canvas.models import FragmentedNarrativeConfig, FragmentedNarrativeRecord
from fragmented_narrative_canvas.validation import validate_record
from fragmented_narrative_canvas.scoring import fragmentation_sensitivity, governance_priority_score, interpretation_readiness, review_priority, trauma_narrative_risk, witness_care


class FragmentedNarrativeCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = FragmentedNarrativeConfig()
        record = FragmentedNarrativeRecord(
            "Test",
            "Context",
            0.8, 0.8, 0.7, 0.8, 0.8, 0.7,
            0.8, 0.7, 0.8, 0.8, 0.7, 0.8,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.8, 0.8, 0.8, 0.8, 0.7,
            "editorial",
            "active",
            "",
        )
        validate_record(record, config)
        for value in [
            fragmentation_sensitivity(record),
            witness_care(record),
            trauma_narrative_risk(record),
            interpretation_readiness(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
