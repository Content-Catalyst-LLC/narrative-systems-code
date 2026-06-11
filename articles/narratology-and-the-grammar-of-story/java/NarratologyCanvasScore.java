public class NarratologyCanvasScore {
    public static double narrativeGrammarStrength(
        double storyDiscourse,
        double voice,
        double focalization,
        double temporalMapping,
        double characterAgency,
        double informationControl
    ) {
        return (storyDiscourse + voice + focalization + temporalMapping + characterAgency + informationControl) / 6.0;
    }

    public static double governanceRisk(
        double omission,
        double powerBlindness,
        double voiceImbalance,
        double closurePressure,
        double unreliableFraming,
        double methodLimits
    ) {
        double score = omission * 0.18 + powerBlindness * 0.20 + voiceImbalance * 0.20 + closurePressure * 0.16 + unreliableFraming * 0.16 + (1.0 - methodLimits) * 0.10;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(narrativeGrammarStrength(0.92, 0.78, 0.74, 0.84, 0.76, 0.82));
        System.out.println(governanceRisk(0.30, 0.28, 0.34, 0.32, 0.36, 0.78));
    }
}
