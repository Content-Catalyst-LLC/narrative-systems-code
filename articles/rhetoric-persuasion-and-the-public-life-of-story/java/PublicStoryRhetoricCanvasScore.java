public class PublicStoryRhetoricCanvasScore {
    public static double rhetoricalBalance(
        double ethosStrength,
        double logosSupport,
        double pathosProportionality,
        double audienceFit,
        double contextClarity
    ) {
        return (
            ethosStrength +
            logosSupport +
            pathosProportionality +
            audienceFit +
            contextClarity
        ) / 5.0;
    }

    public static double publicStoryRisk(
        double verificationStrength,
        double emotionalCoercion,
        double scapegoatingRisk,
        double identityManipulation,
        double closurePressure
    ) {
        double risk =
            (1.0 - verificationStrength) * 0.25 +
            emotionalCoercion * 0.20 +
            scapegoatingRisk * 0.25 +
            identityManipulation * 0.15 +
            closurePressure * 0.15;

        return Math.min(1.0, risk);
    }

    public static void main(String[] args) {
        System.out.println(rhetoricalBalance(0.82, 0.70, 0.78, 0.76, 0.74));
        System.out.println(publicStoryRisk(0.34, 0.82, 0.76, 0.78, 0.84));
    }
}
