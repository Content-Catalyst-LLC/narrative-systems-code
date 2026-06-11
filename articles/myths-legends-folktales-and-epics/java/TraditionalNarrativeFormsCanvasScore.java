public class TraditionalNarrativeFormsCanvasScore {
    public static double formClassification(
        double truthClaimClarity,
        double socialFunction,
        double memoryOrientation,
        double performanceTrace,
        double authorityContext,
        double genreNotes
    ) {
        return (
            truthClaimClarity +
            socialFunction +
            memoryOrientation +
            performanceTrace +
            authorityContext +
            genreNotes
        ) / 6.0;
    }

    public static double adaptationRisk(
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
        System.out.println(formClassification(0.90, 0.88, 0.92, 0.74, 0.86, 0.82));
        System.out.println(adaptationRisk(0.84, 0.88, 0.76, 0.70, 0.86, 0.22));
    }
}
