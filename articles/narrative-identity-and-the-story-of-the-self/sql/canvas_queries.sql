SELECT item, claim_context, (memory_continuity + agency) / 2.0 AS coherence_proxy FROM narrative_identity_claims ORDER BY coherence_proxy DESC;
SELECT item, claim_context, (reduction_risk * 0.45 + forced_coherence * 0.55) AS identity_story_risk FROM narrative_identity_claims ORDER BY identity_story_risk DESC;
