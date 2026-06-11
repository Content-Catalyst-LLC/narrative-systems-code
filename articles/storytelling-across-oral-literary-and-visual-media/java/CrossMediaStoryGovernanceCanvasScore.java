public class CrossMediaStoryGovernanceCanvasScore {
    public static double mediumAffordanceFit(
        double embodiment,
        double interiorDepth,
        double spatialQuality,
        double temporalControl,
        double audienceRelation,
        double contextualFit
    ) {
        return (embodiment + interiorDepth + spatialQuality + temporalControl + audienceRelation + contextualFit) / 6.0;
    }

    public static double mediaTransferRisk(
        double voiceLoss,
        double contextLoss,
        double provenanceLoss,
        double audienceShift,
        double representationalDistortion,
        double governanceReview
    ) {
        double score = voiceLoss * 0.18 + contextLoss * 0.20 + provenanceLoss * 0.18 + audienceShift * 0.14 + representationalDistortion * 0.18 + (1.0 - governanceReview) * 0.12;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(mediumAffordanceFit(0.72, 0.68, 0.42, 0.56, 0.44, 0.62));
        System.out.println(mediaTransferRisk(0.82, 0.76, 0.54, 0.46, 0.58, 0.62));
    }
}
