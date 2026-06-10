public class PlotCoherenceCanvasScore {
    public static double plotCoherence(
        double actionClarity,
        double causalLinkage,
        double motivationVisibility,
        double episodeDependency,
        double turningPointStrength,
        double resolutionConsequence
    ) {
        return (
            actionClarity +
            causalLinkage +
            motivationVisibility +
            episodeDependency +
            turningPointStrength +
            resolutionConsequence
        ) / 6.0;
    }

    public static double coherenceRisk(
        double falseCausality,
        double simplificationBias,
        double closurePressure,
        double evidenceOmission,
        double uncertaintyClarity
    ) {
        double risk =
            falseCausality * 0.25 +
            simplificationBias * 0.20 +
            closurePressure * 0.20 +
            evidenceOmission * 0.20 +
            (1.0 - uncertaintyClarity) * 0.15;

        return Math.min(1.0, risk);
    }

    public static void main(String[] args) {
        System.out.println(plotCoherence(0.86, 0.84, 0.78, 0.82, 0.88, 0.80));
        System.out.println(coherenceRisk(0.52, 0.66, 0.78, 0.58, 0.46));
    }
}
