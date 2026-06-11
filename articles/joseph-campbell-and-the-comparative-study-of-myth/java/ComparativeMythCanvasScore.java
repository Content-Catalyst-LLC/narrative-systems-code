public class ComparativeMythCanvasScore {
    public static double comparativePattern(
        double departurePattern,
        double thresholdCrossing,
        double ordealOrTrial,
        double helperPresence,
        double returnPattern,
        double boonOrRenewal
    ) {
        return (
            departurePattern +
            thresholdCrossing +
            ordealOrTrial +
            helperPresence +
            returnPattern +
            boonOrRenewal
        ) / 6.0;
    }

    public static double generalizationRisk(
        double universalClaimStrength,
        double selectiveEvidence,
        double contextLoss,
        double formulaReduction,
        double ethicalRisk,
        double counterexampleInclusion
    ) {
        double risk =
            universalClaimStrength * 0.18 +
            selectiveEvidence * 0.18 +
            contextLoss * 0.18 +
            formulaReduction * 0.16 +
            ethicalRisk * 0.16 +
            (1.0 - counterexampleInclusion) * 0.14;

        return Math.min(1.0, risk);
    }

    public static void main(String[] args) {
        System.out.println(comparativePattern(0.86, 0.82, 0.88, 0.70, 0.76, 0.74));
        System.out.println(generalizationRisk(0.92, 0.80, 0.84, 0.88, 0.78, 0.20));
    }
}
