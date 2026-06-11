public class LifeWritingCanvasScore {
    public static double lifeWritingCoherence(
        double memoryClarity,
        double temporalStructure,
        double voiceConsistency,
        double agency,
        double relationalGrounding,
        double contextualDepth
    ) {
        return (memoryClarity + temporalStructure + voiceConsistency + agency + relationalGrounding + contextualDepth) / 6.0;
    }

    public static double ethicalRisk(
        double privacyRisk,
        double consentLimits,
        double otherPersonExposure,
        double traumaExtraction,
        double selfMythology,
        double methodLimits
    ) {
        double score = privacyRisk * 0.18 + consentLimits * 0.20 + otherPersonExposure * 0.20 + traumaExtraction * 0.18 + selfMythology * 0.14 + (1.0 - methodLimits) * 0.10;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(lifeWritingCoherence(0.82, 0.88, 0.84, 0.78, 0.76, 0.82));
        System.out.println(ethicalRisk(0.42, 0.38, 0.46, 0.34, 0.52, 0.82));
    }
}
