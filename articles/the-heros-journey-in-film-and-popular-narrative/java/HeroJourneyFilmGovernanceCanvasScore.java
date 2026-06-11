public class HeroJourneyFilmGovernanceCanvasScore {
    public static double heroicArcIntegrity(
        double callAuthenticity,
        double thresholdSignificance,
        double ordealRelevance,
        double valueChange,
        double returnBoon,
        double ethicalConsequence
    ) {
        return (callAuthenticity + thresholdSignificance + ordealRelevance + valueChange + returnBoon + ethicalConsequence) / 6.0;
    }

    public static double formulaRisk(
        double beatCompliance,
        double genericMentor,
        double mechanicalCall,
        double ordealSpectacle,
        double forcedReturn,
        double storyParticularity
    ) {
        double score = beatCompliance * 0.18 + genericMentor * 0.16 + mechanicalCall * 0.18 + ordealSpectacle * 0.16 + forcedReturn * 0.16 + (1.0 - storyParticularity) * 0.16;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(heroicArcIntegrity(0.82, 0.86, 0.70, 0.74, 0.68, 0.66));
        System.out.println(formulaRisk(0.86, 0.78, 0.82, 0.74, 0.76, 0.36));
    }
}
