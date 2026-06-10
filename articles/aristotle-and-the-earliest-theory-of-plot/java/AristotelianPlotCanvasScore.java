public class AristotelianPlotCanvasScore {
    public static double plotUnity(
        double actionClarity,
        double causalLinkage,
        double episodeDependency,
        double turningPointRelevance,
        double resolutionSupport,
        double goalCoherence
    ) {
        return (
            actionClarity +
            causalLinkage +
            episodeDependency +
            turningPointRelevance +
            resolutionSupport +
            goalCoherence
        ) / 6.0;
    }

    public static double formulaRisk(
        double heroTemplateSaturation,
        double closurePressure,
        double unityBias,
        double genreBias,
        double mediumFit
    ) {
        double risk =
            heroTemplateSaturation * 0.20 +
            closurePressure * 0.25 +
            unityBias * 0.20 +
            genreBias * 0.20 +
            (1.0 - mediumFit) * 0.15;

        return Math.min(1.0, risk);
    }

    public static void main(String[] args) {
        System.out.println(plotUnity(0.88, 0.86, 0.84, 0.82, 0.80, 0.84));
        System.out.println(formulaRisk(0.88, 0.84, 0.82, 0.76, 0.54));
    }
}
