public class FolktaleMorphologyCanvasScore {
    public static double functionCoverage(
        double functionIdentification,
        double sequenceClarity,
        double roleMapping,
        double variationTracking,
        double contextNotes
    ) {
        return (
            functionIdentification +
            sequenceClarity +
            roleMapping +
            variationTracking +
            contextNotes
        ) / 5.0;
    }

    public static double reductionRisk(
        double universalizationRisk,
        double culturalErasureRisk,
        double performanceOmission,
        double variationOmission,
        double morphologyContextBalance
    ) {
        double risk =
            universalizationRisk * 0.22 +
            culturalErasureRisk * 0.22 +
            performanceOmission * 0.18 +
            variationOmission * 0.18 +
            (1.0 - morphologyContextBalance) * 0.20;

        return Math.min(1.0, risk);
    }

    public static void main(String[] args) {
        System.out.println(functionCoverage(0.82, 0.78, 0.76, 0.70, 0.72));
        System.out.println(reductionRisk(0.86, 0.82, 0.78, 0.84, 0.22));
    }
}
