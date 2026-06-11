public class MonomythCanvasScore {
    public static double monomythPattern(
        double departurePattern,
        double thresholdCrossing,
        double initiationTrial,
        double descentSymbolicDeath,
        double boon,
        double returnPattern
    ) {
        return (
            departurePattern +
            thresholdCrossing +
            initiationTrial +
            descentSymbolicDeath +
            boon +
            returnPattern
        ) / 6.0;
    }

    public static double formulaDrift(
        double stageLiteralism,
        double beatMatching,
        double contextLoss,
        double overfitting,
        double universalClaimStrength,
        double counterexampleInclusion
    ) {
        double risk =
            stageLiteralism * 0.18 +
            beatMatching * 0.18 +
            contextLoss * 0.18 +
            overfitting * 0.16 +
            universalClaimStrength * 0.16 +
            (1.0 - counterexampleInclusion) * 0.14;

        return Math.min(1.0, risk);
    }

    public static void main(String[] args) {
        System.out.println(monomythPattern(0.88, 0.84, 0.86, 0.72, 0.78, 0.80));
        System.out.println(formulaDrift(0.92, 0.88, 0.86, 0.90, 0.94, 0.18));
    }
}
