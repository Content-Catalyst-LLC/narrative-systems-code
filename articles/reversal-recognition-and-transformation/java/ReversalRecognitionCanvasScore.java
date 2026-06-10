public class ReversalRecognitionCanvasScore {
    public static double reversalIntegrity(
        double preparationTrace,
        double causalLinkage,
        double stateChange,
        double earnedSurprise,
        double actionFit,
        double knowledgeReorientation
    ) {
        return (
            preparationTrace +
            causalLinkage +
            stateChange +
            earnedSurprise +
            actionFit +
            knowledgeReorientation
        ) / 6.0;
    }

    public static double recognitionRisk(
        double falseRecognition,
        double arbitraryTwist,
        double closurePressure,
        double evidenceOmission,
        double uncertaintyClarity
    ) {
        double risk =
            falseRecognition * 0.25 +
            arbitraryTwist * 0.25 +
            closurePressure * 0.20 +
            evidenceOmission * 0.20 +
            (1.0 - uncertaintyClarity) * 0.10;

        return Math.min(1.0, risk);
    }

    public static void main(String[] args) {
        System.out.println(reversalIntegrity(0.86, 0.84, 0.88, 0.82, 0.80, 0.90));
        System.out.println(recognitionRisk(0.88, 0.72, 0.82, 0.84, 0.32));
    }
}
