public class PublicStoryGovernanceCanvasScore {
    public static double publicNarrativeStrength(
        double selfStoryEvidence,
        double sharedValueClarity,
        double nowChallengeClarity,
        double agency,
        double hope,
        double responsibility
    ) {
        return (selfStoryEvidence + sharedValueClarity + nowChallengeClarity + agency + hope + responsibility) / 6.0;
    }

    public static double mythicSimplificationRisk(
        double enemySimplification,
        double boundaryHardening,
        double crisisCompression,
        double urgencyPressure,
        double scapegoatIntensity,
        double evidenceVisibility
    ) {
        double score = enemySimplification * 0.18 + boundaryHardening * 0.18 + crisisCompression * 0.17 + urgencyPressure * 0.16 + scapegoatIntensity * 0.17 + (1.0 - evidenceVisibility) * 0.14;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(publicNarrativeStrength(0.84, 0.82, 0.86, 0.78, 0.80, 0.76));
        System.out.println(mythicSimplificationRisk(0.80, 0.84, 0.86, 0.88, 0.78, 0.46));
    }
}
