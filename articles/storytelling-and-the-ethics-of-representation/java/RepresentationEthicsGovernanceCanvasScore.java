public class RepresentationEthicsGovernanceCanvasScore {
    public static double representationIntegrity(
        double voiceAgency,
        double contextPreservation,
        double dignityProtection,
        double sourceAccuracy,
        double provenanceVisibility,
        double accountabilityCapacity
    ) {
        return (voiceAgency + contextPreservation + dignityProtection + sourceAccuracy + provenanceVisibility + accountabilityCapacity) / 6.0;
    }

    public static double representationRisk(
        double stereotypeTendency,
        double exposureRisk,
        double contextLoss,
        double voiceReplacement,
        double powerAsymmetry,
        double governanceReview
    ) {
        double score = stereotypeTendency * 0.18 + exposureRisk * 0.18 + contextLoss * 0.18 + voiceReplacement * 0.16 + powerAsymmetry * 0.16 + (1.0 - governanceReview) * 0.14;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(representationIntegrity(0.76, 0.74, 0.78, 0.72, 0.70, 0.68));
        System.out.println(representationRisk(0.42, 0.62, 0.46, 0.38, 0.66, 0.72));
    }
}
