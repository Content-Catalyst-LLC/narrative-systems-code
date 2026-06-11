public class AdaptationGovernanceCanvasScore {
    public static double adaptationIntegrity(
        double sourceCore,
        double mediumFit,
        double transformationPurpose,
        double contextPreservation,
        double receptionValue,
        double ethicalGovernance
    ) {
        return (sourceCore + mediumFit + transformationPurpose + contextPreservation + receptionValue + ethicalGovernance) / 6.0;
    }

    public static double transferLoss(
        double voiceLoss,
        double interiorityLoss,
        double contextLoss,
        double provenanceLoss,
        double agencyLoss,
        double governanceReview
    ) {
        double score = voiceLoss * 0.18 + interiorityLoss * 0.16 + contextLoss * 0.20 + provenanceLoss * 0.18 + agencyLoss * 0.16 + (1.0 - governanceReview) * 0.12;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(adaptationIntegrity(0.78, 0.82, 0.76, 0.70, 0.74, 0.68));
        System.out.println(transferLoss(0.42, 0.68, 0.50, 0.38, 0.46, 0.70));
    }
}
