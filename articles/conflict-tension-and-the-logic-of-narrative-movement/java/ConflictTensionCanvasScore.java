public class ConflictTensionCanvasScore {
    public static double conflictClarity(
        double desireClarity,
        double obstacleClarity,
        double pressureStrength,
        double agencyVisibility,
        double stakesVisibility,
        double relationLegibility
    ) {
        return (
            desireClarity +
            obstacleClarity +
            pressureStrength +
            agencyVisibility +
            stakesVisibility +
            relationLegibility
        ) / 6.0;
    }

    public static double conflictRisk(
        double scapegoating,
        double conflictInflation,
        double traumaSpectacle,
        double falseBalance,
        double closurePressure
    ) {
        double risk =
            scapegoating * 0.25 +
            conflictInflation * 0.20 +
            traumaSpectacle * 0.20 +
            falseBalance * 0.20 +
            closurePressure * 0.15;

        return Math.min(1.0, risk);
    }

    public static void main(String[] args) {
        System.out.println(conflictClarity(0.78, 0.74, 0.76, 0.72, 0.80, 0.78));
        System.out.println(conflictRisk(0.84, 0.88, 0.72, 0.74, 0.78));
    }
}
