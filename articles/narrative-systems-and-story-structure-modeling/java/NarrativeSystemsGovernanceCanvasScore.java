public class NarrativeSystemsGovernanceCanvasScore {
    public static double narrativeCoherence(
        double causalAlignment,
        double stateTransitionClarity,
        double agentGoalFit,
        double worldRuleConsistency,
        double temporalMapping,
        double evidenceQuality
    ) {
        return (causalAlignment + stateTransitionClarity + agentGoalFit + worldRuleConsistency + temporalMapping + evidenceQuality) / 6.0;
    }

    public static double formulaDriftRisk(
        double beatTemplateDependence,
        double universalModelClaims,
        double contextLoss,
        double genreFlattening,
        double modelOverconfidence,
        double judgmentReview
    ) {
        double score = beatTemplateDependence * 0.18 + universalModelClaims * 0.18 + contextLoss * 0.18 + genreFlattening * 0.16 + modelOverconfidence * 0.16 + (1.0 - judgmentReview) * 0.14;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(narrativeCoherence(0.82, 0.78, 0.80, 0.76, 0.74, 0.78));
        System.out.println(formulaDriftRisk(0.34, 0.28, 0.32, 0.30, 0.34, 0.82));
    }
}
