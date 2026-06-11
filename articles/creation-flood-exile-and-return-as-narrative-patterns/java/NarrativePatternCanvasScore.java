public class NarrativePatternCanvasScore {
    public static double patternStrength(double creation, double flood, double exile, double returnSignal) {
        return (creation + flood + exile + returnSignal) / 4.0;
    }

    public static double ethicalRisk(
        double originNostalgia,
        double cleansingFantasy,
        double exileRomanticization,
        double falseReturn,
        double powerBlindness,
        double uncertaintyNotes
    ) {
        double score = originNostalgia * 0.18 + cleansingFantasy * 0.20 + exileRomanticization * 0.18 + falseReturn * 0.18 + powerBlindness * 0.16 + (1.0 - uncertaintyNotes) * 0.10;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(patternStrength(0.96, 0.20, 0.24, 0.42));
        System.out.println(ethicalRisk(0.38, 0.20, 0.24, 0.30, 0.32, 0.74));
    }
}
