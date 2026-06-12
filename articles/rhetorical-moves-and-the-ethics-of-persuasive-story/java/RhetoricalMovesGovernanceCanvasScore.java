public class RhetoricalMovesGovernanceCanvasScore {
    public static double rhetoricalIntegrity(
        double evidenceTruthfulness,
        double proportionality,
        double contextAdequacy,
        double dignityProtection,
        double audienceAgency,
        double transparency
    ) {
        return (evidenceTruthfulness + proportionality + contextAdequacy + dignityProtection + audienceAgency + transparency) / 6.0;
    }

    public static double manipulationRisk(
        double fearAmplification,
        double emotionalExploitation,
        double omissionOfContext,
        double socialProofPressure,
        double urgencyCoercion,
        double judgmentReview
    ) {
        double score = fearAmplification * 0.18 + emotionalExploitation * 0.18 + omissionOfContext * 0.18 + socialProofPressure * 0.16 + urgencyCoercion * 0.16 + (1.0 - judgmentReview) * 0.14;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(rhetoricalIntegrity(0.82, 0.78, 0.80, 0.82, 0.76, 0.78));
        System.out.println(manipulationRisk(0.34, 0.36, 0.32, 0.38, 0.42, 0.82));
    }
}
