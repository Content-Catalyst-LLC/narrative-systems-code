public class StorytellingHeritageCanvasScore {
    public static double livingContinuity(
        double transmissionSupport,
        double performanceContext,
        double languageVitality,
        double apprenticeshipPathways,
        double communityRecognition,
        double variationManagement
    ) {
        return (
            transmissionSupport +
            performanceContext +
            languageVitality +
            apprenticeshipPathways +
            communityRecognition +
            variationManagement
        ) / 6.0;
    }

    public static double archiveRisk(
        double contextRemoval,
        double sacredOrRestrictedMaterial,
        double performanceOmission,
        double translationLoss,
        double extractionRisk,
        double governanceControl
    ) {
        double risk =
            contextRemoval * 0.18 +
            sacredOrRestrictedMaterial * 0.22 +
            performanceOmission * 0.16 +
            translationLoss * 0.16 +
            extractionRisk * 0.18 +
            (1.0 - governanceControl) * 0.10;

        return Math.min(1.0, risk);
    }

    public static void main(String[] args) {
        System.out.println(livingContinuity(0.86, 0.82, 0.76, 0.78, 0.84, 0.80));
        System.out.println(archiveRisk(0.82, 0.64, 0.78, 0.66, 0.84, 0.18));
    }
}
