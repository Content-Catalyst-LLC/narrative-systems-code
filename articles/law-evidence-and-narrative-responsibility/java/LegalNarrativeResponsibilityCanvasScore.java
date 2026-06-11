public class LegalNarrativeResponsibilityCanvasScore {
    public static double evidenceSupport(
        double relevance,
        double authentication,
        double provenance,
        double corroboration,
        double crossChecking,
        double uncertaintyNotation
    ) {
        return (relevance + authentication + provenance + corroboration + crossChecking + uncertaintyNotation) / 6.0;
    }

    public static double narrativeOverreachRisk(
        double overcoherence,
        double evidentiaryGap,
        double stereotypeReliance,
        double causationFlattening,
        double affectiveBias,
        double uncertaintyVisibility
    ) {
        double score = overcoherence * 0.18 + evidentiaryGap * 0.18 + stereotypeReliance * 0.16 + causationFlattening * 0.16 + affectiveBias * 0.16 + (1.0 - uncertaintyVisibility) * 0.16;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(evidenceSupport(0.82, 0.76, 0.74, 0.70, 0.78, 0.68));
        System.out.println(narrativeOverreachRisk(0.84, 0.86, 0.66, 0.78, 0.72, 0.34));
    }
}
