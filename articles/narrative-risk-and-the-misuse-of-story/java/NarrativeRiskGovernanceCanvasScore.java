public class NarrativeRiskGovernanceCanvasScore {
    public static double narrativeRisk(
        double scapegoating,
        double evidenceImmunity,
        double mythicSimplification,
        double contextLoss,
        double groupBlameIntensity,
        double revisionOpenness
    ) {
        double score = scapegoating * 0.18 + evidenceImmunity * 0.20 + mythicSimplification * 0.18 + contextLoss * 0.16 + groupBlameIntensity * 0.16 + (1.0 - revisionOpenness) * 0.12;
        return Math.min(1.0, score);
    }

    public static double evidenceIntegrity(
        double corroboration,
        double sourceQuality,
        double timelineClarity,
        double uncertaintyDisclosure,
        double accountabilityClarity,
        double disconfirmationOpenness
    ) {
        return (corroboration + sourceQuality + timelineClarity + uncertaintyDisclosure + accountabilityClarity + disconfirmationOpenness) / 6.0;
    }

    public static void main(String[] args) {
        System.out.println(narrativeRisk(0.24, 0.28, 0.30, 0.34, 0.20, 0.78));
        System.out.println(evidenceIntegrity(0.72, 0.70, 0.74, 0.68, 0.76, 0.72));
    }
}
