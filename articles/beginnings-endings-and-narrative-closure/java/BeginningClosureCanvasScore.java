public class BeginningClosureCanvasScore {
    public static double openingClarity(
        double voiceSignal,
        double worldOrientation,
        double pressureIntroduction,
        double stakesVisibility,
        double questionFraming,
        double contractTransparency
    ) {
        return (
            voiceSignal +
            worldOrientation +
            pressureIntroduction +
            stakesVisibility +
            questionFraming +
            contractTransparency
        ) / 6.0;
    }

    public static double closureRisk(
        double prematureRepair,
        double falseResolution,
        double systemFlattening,
        double aftermathOmission,
        double excessiveAudienceComfort
    ) {
        double risk =
            prematureRepair * 0.24 +
            falseResolution * 0.24 +
            systemFlattening * 0.20 +
            aftermathOmission * 0.18 +
            excessiveAudienceComfort * 0.14;

        return Math.min(1.0, risk);
    }

    public static void main(String[] args) {
        System.out.println(openingClarity(0.82, 0.70, 0.72, 0.76, 0.80, 0.74));
        System.out.println(closureRisk(0.82, 0.78, 0.74, 0.84, 0.70));
    }
}
