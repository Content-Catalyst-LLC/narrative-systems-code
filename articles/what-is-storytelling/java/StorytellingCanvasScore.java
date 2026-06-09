public class StorytellingCanvasScore {
    public static double coherenceScore(
        double sequenceClarity,
        double agencyClarity,
        double causalConnection,
        double transformationClarity,
        double interpretiveRelevance
    ) {
        return (
            sequenceClarity +
            agencyClarity +
            causalConnection +
            transformationClarity +
            interpretiveRelevance
        ) / 5.0;
    }

    public static double governanceRisk(
        double evidenceStrength,
        double representationCare,
        double persuasiveIntensity,
        double audienceConsequence
    ) {
        double risk =
            (1.0 - evidenceStrength) * 0.30 +
            (1.0 - representationCare) * 0.30 +
            persuasiveIntensity * 0.20 +
            audienceConsequence * 0.20;

        return Math.min(1.0, risk);
    }

    public static void main(String[] args) {
        System.out.println(coherenceScore(0.82, 0.78, 0.74, 0.76, 0.84));
        System.out.println(governanceRisk(0.56, 0.54, 0.88, 0.86));
    }
}
