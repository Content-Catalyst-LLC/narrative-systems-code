public class PostcolonialNarrativeFormCanvasScore {
    public static double colonialFormRisk(
        double archiveDominance,
        double languageHierarchy,
        double gazeCentrality,
        double templateForcing,
        double extractionAnxiety,
        double opacityProtection
    ) {
        double score = archiveDominance * 0.18 + languageHierarchy * 0.18 + gazeCentrality * 0.18 + templateForcing * 0.18 + extractionAnxiety * 0.16 + (1.0 - opacityProtection) * 0.12;
        return Math.min(1.0, score);
    }

    public static double digitalColoniality(
        double englishDominance,
        double stereotypeBias,
        double extractionRisk,
        double archiveFlattening,
        double visualOrientalism,
        double communityGovernance
    ) {
        double score = englishDominance * 0.18 + stereotypeBias * 0.18 + extractionRisk * 0.18 + archiveFlattening * 0.16 + visualOrientalism * 0.16 + (1.0 - communityGovernance) * 0.14;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(colonialFormRisk(0.74, 0.52, 0.66, 0.58, 0.62, 0.80));
        System.out.println(digitalColoniality(0.92, 0.90, 0.86, 0.78, 0.84, 0.42));
    }
}
