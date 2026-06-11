public class UniversalStoryModelCanvasScore {
    public static double universalModelFit(
        double stageEvidence,
        double agencyMatch,
        double transformationCorrespondence,
        double contextualHarmony,
        double resolutionSimilarity,
        double evidenceVisibility
    ) {
        return (stageEvidence + agencyMatch + transformationCorrespondence + contextualHarmony + resolutionSimilarity + evidenceVisibility) / 6.0;
    }

    public static double universalismRisk(
        double archiveBias,
        double genderBinaryPressure,
        double culturalFlattening,
        double intersectionalErasure,
        double queerTransPressure,
        double localContext
    ) {
        double score = archiveBias * 0.18 + genderBinaryPressure * 0.20 + culturalFlattening * 0.18 + intersectionalErasure * 0.18 + queerTransPressure * 0.16 + (1.0 - localContext) * 0.10;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(universalModelFit(0.82, 0.76, 0.78, 0.62, 0.72, 0.80));
        System.out.println(universalismRisk(0.70, 0.82, 0.66, 0.62, 0.58, 0.64));
    }
}
