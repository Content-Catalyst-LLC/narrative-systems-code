import unittest
from narrative_identity_canvas.models import NarrativeIdentityConfig, NarrativeIdentityRecord
from narrative_identity_canvas.validation import validate_record
from narrative_identity_canvas.scoring import governance_priority_score, identity_story_risk, interpretation_readiness, narrative_coherence, review_priority, revision_readiness
class NarrativeIdentityCanvasTests(unittest.TestCase):
    def test_scores_are_bounded(self):
        c=NarrativeIdentityConfig(); r=NarrativeIdentityRecord("Test","Context",0.8,0.8,0.7,0.8,0.8,0.7,0.8,0.7,0.8,0.7,0.8,0.8,0.3,0.4,0.3,0.4,0.3,0.8,0.8,0.7,0.8,0.8,0.7,"editorial","active","")
        validate_record(r,c)
        for v in [narrative_coherence(r),revision_readiness(r),identity_story_risk(r),interpretation_readiness(r),governance_priority_score(r,c)]: self.assertGreaterEqual(v,0); self.assertLessEqual(v,1)
        self.assertIn(review_priority(r,c),{"standard","medium","high"})
if __name__=="__main__": unittest.main()
