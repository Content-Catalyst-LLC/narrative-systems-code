from __future__ import annotations

import unittest

from non_heroic_narrative_canvas.models import NonHeroicNarrativeConfig, NonHeroicNarrativeRecord
from non_heroic_narrative_canvas.validation import validate_record
from non_heroic_narrative_canvas.scoring import cyclical_structure, governance_priority_score, heroic_overfit_risk, non_heroic_agency, review_priority, review_readiness, tragic_structure


class NonHeroicNarrativeCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = NonHeroicNarrativeConfig()
        record = NonHeroicNarrativeRecord(
            "Test",
            "Context",
            0.8, 0.7, 0.6, 0.7, 0.8, 0.7,
            0.6, 0.5, 0.6, 0.5, 0.4, 0.6,
            0.8, 0.8, 0.7, 0.6, 0.8, 0.8,
            0.4, 0.4, 0.4, 0.4, 0.4, 0.8,
            0.7, 0.8, 0.8, 0.8, 0.8,
            "editorial",
            "active",
            "",
        )
        validate_record(record, config)
        for value in [
            tragic_structure(record),
            cyclical_structure(record),
            non_heroic_agency(record),
            heroic_overfit_risk(record),
            review_readiness(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
