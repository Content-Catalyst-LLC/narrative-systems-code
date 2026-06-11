public class ComparativeStoryGovernanceCanvasScore {
    public static double comparativeIntegrity(
        double sourceContext,
        double differencePreservation,
        double evidenceQuality,
        double translationReliability,
        double protocolCompliance,
        double humanReview
    ) {
        return (sourceContext + differencePreservation + evidenceQuality + translationReliability + protocolCompliance + humanReview) / 6.0;
    }

    public static double flatteningRisk(
        double universalismClaims,
        double templateCapture,
        double contextLoss,
        double archiveBias,
        double powerImbalance,
        double differencePreservation
    ) {
        double score = universalismClaims * 0.18 + templateCapture * 0.18 + contextLoss * 0.18 + archiveBias * 0.16 + powerImbalance * 0.16 + (1.0 - differencePreservation) * 0.14;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(comparativeIntegrity(0.76, 0.78, 0.74, 0.70, 0.72, 0.80));
        System.out.println(flatteningRisk(0.54, 0.42, 0.48, 0.46, 0.50, 0.78));
    }
}
