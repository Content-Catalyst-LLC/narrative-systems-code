public class NarrativeUnderstandingCanvasScore {
    public static double understandingScore(
        double sequenceClarity,
        double causalFraming,
        double agencyMapping,
        double memoryIntegration,
        double evidenceSupport,
        double opennessToRevision
    ) {
        return (
            sequenceClarity +
            causalFraming +
            agencyMapping +
            memoryIntegration +
            evidenceSupport +
            opennessToRevision
        ) / 6.0;
    }

    public static double overreachRisk(
        double evidenceSupport,
        double hindsightBias,
        double falseCoherence,
        double selectionBias,
        double closurePressure
    ) {
        double risk =
            (1.0 - evidenceSupport) * 0.25 +
            hindsightBias * 0.20 +
            falseCoherence * 0.25 +
            selectionBias * 0.15 +
            closurePressure * 0.15;

        return Math.min(1.0, risk);
    }

    public static void main(String[] args) {
        System.out.println(understandingScore(0.84, 0.76, 0.78, 0.86, 0.72, 0.70));
        System.out.println(overreachRisk(0.50, 0.70, 0.78, 0.66, 0.72));
    }
}
