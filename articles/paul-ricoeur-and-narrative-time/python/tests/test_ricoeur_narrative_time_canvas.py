from __future__ import annotations

import unittest

from ricoeur_narrative_time_canvas.models import NarrativeTimeConfig, NarrativeTimeRecord
from ricoeur_narrative_time_canvas.validation import validate_record
from ricoeur_narrative_time_canvas.scoring import emplotment_strength, governance_priority_score, interpretation_readiness, narrative_identity_readiness, narrative_time_configuration, review_priority, temporal_governance_risk


class RicoeurNarrativeTimeCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self) -> None:
        config = NarrativeTimeConfig()
        record = NarrativeTimeRecord(
            "Test",
            "Context",
            0.8, 0.8, 0.7, 0.8, 0.8, 0.7,
            0.8, 0.7, 0.7, 0.8, 0.7, 0.8,
            0.8, 0.8, 0.7, 0.7, 0.8, 0.8,
            0.3, 0.4, 0.3, 0.4, 0.3, 0.8,
            0.8, 0.7, 0.8,
            "editorial",
            "active",
            "",
        )
        validate_record(record, config)
        for value in [narrative_time_configuration(record), emplotment_strength(record), narrative_identity_readiness(record), temporal_governance_risk(record), interpretation_readiness(record), governance_priority_score(record, config)]:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertIn(review_priority(record, config), {"standard", "medium", "high"})


if __name__ == "__main__":
    unittest.main()
