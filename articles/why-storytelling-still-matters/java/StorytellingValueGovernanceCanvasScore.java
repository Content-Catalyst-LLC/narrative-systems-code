public class StorytellingValueGovernanceCanvasScore {
    public static double storytellingValue(
        double clarity,
        double evidenceGrounding,
        double memoryContinuity,
        double audienceReasoning,
        double dignityProtection,
        double publicUsefulness
    ) {
        return (clarity + evidenceGrounding + memoryContinuity + audienceReasoning + dignityProtection + publicUsefulness) / 6.0;
    }

    public static double misuseRisk(
        double oversimplification,
        double emotionalExploitation,
        double scapegoating,
        double contextLoss,
        double platformFrictionlessness,
        double humanReview
    ) {
        double score = oversimplification * 0.18 + emotionalExploitation * 0.18 + scapegoating * 0.18 + contextLoss * 0.18 + platformFrictionlessness * 0.14 + (1.0 - humanReview) * 0.14;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(storytellingValue(0.86, 0.82, 0.92, 0.80, 0.88, 0.84));
        System.out.println(misuseRisk(0.22, 0.20, 0.16, 0.24, 0.30, 0.88));
    }
}
