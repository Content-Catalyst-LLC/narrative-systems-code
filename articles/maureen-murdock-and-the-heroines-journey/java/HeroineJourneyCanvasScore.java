public class HeroineJourneyCanvasScore {
    public static double heroineAlignment(
        double separationFromFeminine,
        double masculineIdentification,
        double aridityAfterSuccess,
        double descentCrisis,
        double reconnectionFeminine,
        double integrationWholeness
    ) {
        return (separationFromFeminine + masculineIdentification + aridityAfterSuccess + descentCrisis + reconnectionFeminine + integrationWholeness) / 6.0;
    }

    public static double frameworkRisk(
        double templateForcing,
        double genderEssentialism,
        double universalWomanhood,
        double psychologicalOverreach,
        double healingPressure,
        double culturalContext
    ) {
        double score = templateForcing * 0.20 + genderEssentialism * 0.20 + universalWomanhood * 0.18 + psychologicalOverreach * 0.18 + healingPressure * 0.14 + (1.0 - culturalContext) * 0.10;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(heroineAlignment(0.82, 0.88, 0.86, 0.78, 0.76, 0.74));
        System.out.println(frameworkRisk(0.36, 0.42, 0.38, 0.34, 0.40, 0.84));
    }
}
