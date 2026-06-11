public class FourFunctionMythCanvasScore {
    public static double culturalWork(double mystical, double cosmological, double sociological, double pedagogical, double ritualMemory, double authorityClarity) {
        return (mystical + cosmological + sociological + pedagogical + ritualMemory + authorityClarity) / 6.0;
    }

    public static double sociologicalRisk(double hierarchy, double exclusion, double compliance, double omission, double powerInvisibility, double accountability) {
        double score = hierarchy * 0.20 + exclusion * 0.20 + compliance * 0.18 + omission * 0.16 + powerInvisibility * 0.16 + (1.0 - accountability) * 0.10;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(culturalWork(0.92, 0.96, 0.72, 0.78, 0.86, 0.82));
        System.out.println(sociologicalRisk(0.70, 0.64, 0.58, 0.78, 0.72, 0.42));
    }
}
