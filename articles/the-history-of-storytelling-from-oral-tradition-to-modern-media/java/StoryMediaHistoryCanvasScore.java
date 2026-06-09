public class StoryMediaHistoryCanvasScore {
    public static double transmissionStrength(
        double preservation,
        double repeatability,
        double circulation,
        double archiveDurability
    ) {
        return (
            preservation +
            repeatability +
            circulation +
            archiveDurability
        ) / 4.0;
    }

    public static double preservationRisk(
        double archiveDurability,
        double governanceComplexity,
        double contextRetention,
        double accessOpenness,
        double platformStability
    ) {
        double risk =
            (1.0 - archiveDurability) * 0.25 +
            governanceComplexity * 0.20 +
            (1.0 - contextRetention) * 0.25 +
            (1.0 - accessOpenness) * 0.15 +
            (1.0 - platformStability) * 0.15;

        return Math.min(1.0, risk);
    }

    public static void main(String[] args) {
        System.out.println(transmissionStrength(0.68, 0.74, 0.96, 0.54));
        System.out.println(preservationRisk(0.54, 0.92, 0.44, 0.78, 0.38));
    }
}
