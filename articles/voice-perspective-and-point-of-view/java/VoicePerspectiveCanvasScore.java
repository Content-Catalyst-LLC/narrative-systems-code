public class VoicePerspectiveCanvasScore {
    public static double voiceConsistency(
        double toneStability,
        double dictionCoherence,
        double rhetoricalHabit,
        double addressStability,
        double judgmentCoherence
    ) {
        return (
            toneStability +
            dictionCoherence +
            rhetoricalHabit +
            addressStability +
            judgmentCoherence
        ) / 5.0;
    }

    public static double reliabilityRisk(
        double factualUnreliability,
        double interpretiveUnreliability,
        double ethicalUnreliability,
        double memoryDistortion,
        double agencyGap
    ) {
        double risk =
            factualUnreliability * 0.20 +
            interpretiveUnreliability * 0.20 +
            ethicalUnreliability * 0.20 +
            memoryDistortion * 0.20 +
            agencyGap * 0.20;

        return Math.min(1.0, risk);
    }

    public static void main(String[] args) {
        System.out.println(voiceConsistency(0.78, 0.82, 0.76, 0.80, 0.74));
        System.out.println(reliabilityRisk(0.62, 0.70, 0.58, 0.50, 0.66));
    }
}
