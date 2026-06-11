public class ThresholdOrdealCanvasScore {
    public static double ethicalRisk(double harm, double spectacle, double closure, double contextLoss, double powerHiding, double unresolved) {
        double score = harm * 0.20 + spectacle * 0.18 + closure * 0.18 + contextLoss * 0.16 + powerHiding * 0.16 + (1.0 - unresolved) * 0.12;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(ethicalRisk(0.88, 0.82, 0.86, 0.84, 0.90, 0.18));
    }
}
