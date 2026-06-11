public class FragmentedNarrativeCanvasScore {
    public static double fragmentationSensitivity(
        double temporalRupture,
        double gapMarking,
        double repetitionPatterning,
        double silenceRespect,
        double uncertaintyNotes,
        double contextualCare
    ) {
        return (temporalRupture + gapMarking + repetitionPatterning + silenceRespect + uncertaintyNotes + contextualCare) / 6.0;
    }

    public static double traumaNarrativeRisk(
        double forcedCoherence,
        double redemptiveShortcut,
        double extractionRisk,
        double identityReduction,
        double spectaclePressure,
        double methodLimits
    ) {
        double score = forcedCoherence * 0.20 + redemptiveShortcut * 0.18 + extractionRisk * 0.20 + identityReduction * 0.18 + spectaclePressure * 0.14 + (1.0 - methodLimits) * 0.10;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(fragmentationSensitivity(0.88, 0.82, 0.84, 0.90, 0.86, 0.84));
        System.out.println(traumaNarrativeRisk(0.42, 0.46, 0.58, 0.48, 0.52, 0.84));
    }
}
