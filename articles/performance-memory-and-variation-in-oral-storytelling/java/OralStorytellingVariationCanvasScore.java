public class OralStorytellingVariationCanvasScore {
    public static double performanceContext(
        double tellerRole,
        double audienceDocumentation,
        double occasionContext,
        double placeLinkage,
        double embodiment,
        double interactionNotes
    ) {
        return (
            tellerRole +
            audienceDocumentation +
            occasionContext +
            placeLinkage +
            embodiment +
            interactionNotes
        ) / 6.0;
    }

    public static double archiveRisk(
        double fixationRisk,
        double contextRemoval,
        double performanceOmission,
        double translationLoss,
        double extractionRisk,
        double governanceControl
    ) {
        double risk =
            fixationRisk * 0.18 +
            contextRemoval * 0.18 +
            performanceOmission * 0.18 +
            translationLoss * 0.14 +
            extractionRisk * 0.18 +
            (1.0 - governanceControl) * 0.14;

        return Math.min(1.0, risk);
    }

    public static void main(String[] args) {
        System.out.println(performanceContext(0.84, 0.82, 0.78, 0.70, 0.88, 0.86));
        System.out.println(archiveRisk(0.86, 0.88, 0.82, 0.64, 0.84, 0.18));
    }
}
