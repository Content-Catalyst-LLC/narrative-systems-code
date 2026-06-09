public class CulturalStoryCanvasScore {
    public static double culturalValueScore(
        double memoryFunction,
        double teachingValue,
        double identityFunction,
        double belongingFunction,
        double moralImagination,
        double socialCoordination
    ) {
        return (
            memoryFunction +
            teachingValue +
            identityFunction +
            belongingFunction +
            moralImagination +
            socialCoordination
        ) / 6.0;
    }

    public static double narrativeRisk(
        double sourceTransparency,
        double representationCare,
        double persuasiveIntensity,
        double audienceConsequence
    ) {
        double risk =
            persuasiveIntensity * 0.25 +
            (1.0 - sourceTransparency) * 0.25 +
            (1.0 - representationCare) * 0.30 +
            audienceConsequence * 0.20;

        return Math.min(1.0, risk);
    }

    public static void main(String[] args) {
        System.out.println(culturalValueScore(0.88, 0.86, 0.78, 0.82, 0.76, 0.70));
        System.out.println(narrativeRisk(0.54, 0.50, 0.90, 0.92));
    }
}
