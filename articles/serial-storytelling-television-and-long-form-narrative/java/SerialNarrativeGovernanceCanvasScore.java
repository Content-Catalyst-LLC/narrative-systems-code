public class SerialNarrativeGovernanceCanvasScore {
    public static double seasonCoherence(
        double episodeFunction,
        double arcProgression,
        double thematicDevelopment,
        double characterMemory,
        double payoffIntegritySignal,
        double finaleConsequence
    ) {
        return (episodeFunction + arcProgression + thematicDevelopment + characterMemory + payoffIntegritySignal + finaleConsequence) / 6.0;
    }

    public static double continuityBurden(
        double unresolvedArcs,
        double loreDensity,
        double memoryExpectation,
        double recapUncertainty,
        double continuitySaturation,
        double audienceAccessibility
    ) {
        double score = unresolvedArcs * 0.20 + loreDensity * 0.16 + memoryExpectation * 0.18 + recapUncertainty * 0.14 + continuitySaturation * 0.18 + (1.0 - audienceAccessibility) * 0.14;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(seasonCoherence(0.82, 0.78, 0.80, 0.76, 0.74, 0.72));
        System.out.println(continuityBurden(0.46, 0.52, 0.58, 0.42, 0.48, 0.70));
    }
}
