public class RicoeurNarrativeTimeCanvasScore {
    public static double narrativeTimeConfiguration(
        double memoryMapping,
        double anticipation,
        double plotLogic,
        double configuration,
        double refiguration,
        double endingFunction
    ) {
        return (memoryMapping + anticipation + plotLogic + configuration + refiguration + endingFunction) / 6.0;
    }

    public static double temporalGovernanceRisk(
        double prematureClosure,
        double redemptiveShortcut,
        double erasedContinuity,
        double delayedAccountability,
        double nostalgicOrigin,
        double uncertaintyNotes
    ) {
        double score = prematureClosure * 0.20 + redemptiveShortcut * 0.18 + erasedContinuity * 0.18 + delayedAccountability * 0.18 + nostalgicOrigin * 0.14 + (1.0 - uncertaintyNotes) * 0.12;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(narrativeTimeConfiguration(0.84, 0.82, 0.88, 0.94, 0.92, 0.80));
        System.out.println(temporalGovernanceRisk(0.30, 0.28, 0.34, 0.36, 0.32, 0.82));
    }
}
