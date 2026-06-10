public class MeaningArchitectureCanvasScore {
    public static double temporalCoherence(
        double originClarity,
        double sequenceClarity,
        double continuitySupport,
        double ruptureRecognition,
        double futureProjection,
        double governanceVisibility
    ) {
        return (
            originClarity +
            sequenceClarity +
            continuitySupport +
            ruptureRecognition +
            futureProjection +
            governanceVisibility
        ) / 6.0;
    }

    public static double driftRisk(
        double evidenceStrength,
        double sourceAge,
        double linkBreakage,
        double contextRetention,
        double repetitionStrength
    ) {
        double risk =
            (1.0 - evidenceStrength) * 0.25 +
            sourceAge * 0.20 +
            linkBreakage * 0.20 +
            (1.0 - contextRetention) * 0.20 +
            repetitionStrength * 0.15;

        return Math.min(1.0, risk);
    }

    public static void main(String[] args) {
        System.out.println(temporalCoherence(0.88, 0.86, 0.82, 0.78, 0.84, 0.86));
        System.out.println(driftRisk(0.58, 0.56, 0.22, 0.48, 0.92));
    }
}
