from __future__ import annotations

import unittest

from hero_journey_film_governance_canvas.models import HeroJourneyFilmGovernanceConfig, HeroJourneyFilmGovernanceRecord
from hero_journey_film_governance_canvas.validation import validate_record
from hero_journey_film_governance_canvas.scoring import ai_hero_template_risk, cinematic_transformation, culture_gender_integrity, formula_risk, governance_priority_score, heroic_arc_integrity, review_priority


class HeroJourneyFilmGovernanceCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = HeroJourneyFilmGovernanceConfig()
        record = HeroJourneyFilmGovernanceRecord(
            "Test", "Context",
            0.8, 0.8, 0.7, 0.8, 0.7, 0.8,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.8, 0.8, 0.7, 0.7, 0.8, 0.8,
            0.8, 0.8, 0.7, 0.7,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.7,
            "editorial", "active", ""
        )
        validate_record(record, config)
        for value in [
            heroic_arc_integrity(record),
            formula_risk(record),
            cinematic_transformation(record),
            culture_gender_integrity(record),
            ai_hero_template_risk(record),
            governance_priority_score(record, config),
        ]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
