public class OralTraditionCanvasScore {
    public static double performanceContext(
        double tellerRole,
        double audienceResponse,
        double occasionClarity,
        double embodiment,
        double settingPlace,
        double culturalFrame
    ) {
        return (
            tellerRole +
            audienceResponse +
            occasionClarity +
            embodiment +
            settingPlace +
            culturalFrame
        ) / 6.0;
    }

    public static double archiveRisk(
        double consentLimits,
        double restrictedKnowledge,
        double exposureRisk,
        double ownershipRisk,
        double extractionRisk,
        double governanceControl
    ) {
        double risk =
            consentLimits * 0.18 +
            restrictedKnowledge * 0.22 +
            exposureRisk * 0.18 +
            ownershipRisk * 0.18 +
            extractionRisk * 0.14 +
            (1.0 - governanceControl) * 0.10;

        return Math.min(1.0, risk);
    }

    public static void main(String[] args) {
        System.out.println(performanceContext(0.92, 0.82, 0.86, 0.88, 0.74, 0.86));
        System.out.println(archiveRisk(0.82, 0.76, 0.80, 0.88, 0.90, 0.20));
    }
}
