public class PublicNarrativeGovernanceCanvasScore {
    public static double publicNarrativeCoherence(
        double selfClarity,
        double usClarity,
        double nowClarity,
        double valueArticulation,
        double actionClarity,
        double governanceReview
    ) {
        return (selfClarity + usClarity + nowClarity + valueArticulation + actionClarity + governanceReview) / 6.0;
    }

    public static double testimonyExtractionRisk(
        double consentDeficit,
        double emotionalTargeting,
        double safetyRisk,
        double reuseUncertainty,
        double visibilityRisk,
        double agency
    ) {
        double score = consentDeficit * 0.18 + emotionalTargeting * 0.18 + safetyRisk * 0.18 + reuseUncertainty * 0.16 + visibilityRisk * 0.16 + (1.0 - agency) * 0.14;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(publicNarrativeCoherence(0.84, 0.80, 0.76, 0.82, 0.72, 0.68));
        System.out.println(testimonyExtractionRisk(0.68, 0.76, 0.72, 0.70, 0.78, 0.42));
    }
}
