public class CompactOralFormsCanvasScore {
    public static double oralFormContext(
        double formIdentification,
        double speakerRole,
        double audienceDocumentation,
        double occasionNotes,
        double placeLinkage,
        double useContext
    ) {
        return (
            formIdentification +
            speakerRole +
            audienceDocumentation +
            occasionNotes +
            placeLinkage +
            useContext
        ) / 6.0;
    }

    public static double archiveRisk(
        double quoteExtractionRisk,
        double contextRemoval,
        double soundLoss,
        double translationLoss,
        double extractionRisk,
        double governanceControl
    ) {
        double risk =
            quoteExtractionRisk * 0.18 +
            contextRemoval * 0.18 +
            soundLoss * 0.16 +
            translationLoss * 0.16 +
            extractionRisk * 0.18 +
            (1.0 - governanceControl) * 0.14;

        return Math.min(1.0, risk);
    }

    public static void main(String[] args) {
        System.out.println(oralFormContext(0.92, 0.78, 0.72, 0.82, 0.58, 0.88));
        System.out.println(archiveRisk(0.92, 0.88, 0.74, 0.76, 0.94, 0.16));
    }
}
