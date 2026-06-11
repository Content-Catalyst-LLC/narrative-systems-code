import unittest
from catalyst_canvas.models import CanvasConfig, CanvasRecord
from catalyst_canvas.validation import validate_config, validate_record
from catalyst_canvas.scoring import domain_strength, risk_score, interpretation_readiness, governance_priority_score, review_priority
class CatalystCanvasAdvancedTests(unittest.TestCase):
    def test_scores_are_bounded(self):
        c=CanvasConfig("Narrative Identity and the Story of the Self","narrative-identity-and-the-story-of-the-self","catalyst_canvas",{"source_context":1,"conceptual_depth":1},{"context_loss":1,"power_blindness":1},{"method_limits":1,"counterexamples":1},{"medium":0.45,"high":0.62}); validate_config(c)
        r=CanvasRecord("Claim","Context",c.article_title,c.article_slug,{"source_context":0.8,"conceptual_depth":0.7},{"context_loss":0.2,"power_blindness":0.3},{"method_limits":0.8,"counterexamples":0.7},"editorial","active")
        validate_record(r,c)
        for v in [domain_strength(r,c),risk_score(r,c),interpretation_readiness(r,c),governance_priority_score(r,c)]: self.assertGreaterEqual(v,0); self.assertLessEqual(v,1)
        self.assertIn(review_priority(r,c),{"standard","medium","high"})
if __name__=="__main__": unittest.main()
