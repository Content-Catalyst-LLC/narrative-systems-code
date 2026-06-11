public class DigitalStorytellingGovernanceCanvasScore {
    public static double platformNarrativeIntegrity(
        double contextPreservation,
        double sourceAuthority,
        double visibilityProvenanceFit,
        double audienceCare,
        double mediumFormatFit,
        double ethicalGovernance
    ) {
        return (contextPreservation + sourceAuthority + visibilityProvenanceFit + audienceCare + mediumFormatFit + ethicalGovernance) / 6.0;
    }

    public static double contextCollapseRisk(
        double audienceSpread,
        double compressionSeverity,
        double hostileContextExposure,
        double engagementIntensity,
        double sensitiveVisibility,
        double governanceReview
    ) {
        double score = audienceSpread * 0.18 + compressionSeverity * 0.16 + hostileContextExposure * 0.18 + engagementIntensity * 0.14 + sensitiveVisibility * 0.18 + (1.0 - governanceReview) * 0.16;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(platformNarrativeIntegrity(0.78, 0.76, 0.72, 0.74, 0.80, 0.70));
        System.out.println(contextCollapseRisk(0.58, 0.66, 0.52, 0.62, 0.70, 0.74));
    }
}
