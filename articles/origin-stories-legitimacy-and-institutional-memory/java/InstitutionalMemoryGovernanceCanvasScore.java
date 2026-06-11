public class InstitutionalMemoryGovernanceCanvasScore {
    public static double legitimacyAlignment(
        double purposeClarity,
        double missionActionAlignment,
        double recordEvidence,
        double affectedCommunityTestimony,
        double conductVisibility,
        double governanceOpenness
    ) {
        return (purposeClarity + missionActionAlignment + recordEvidence + affectedCommunityTestimony + conductVisibility + governanceOpenness) / 6.0;
    }

    public static double originMythRisk(
        double founderHeroization,
        double exclusionOmission,
        double harmRemoval,
        double commemorationSaturation,
        double reputationalBranding,
        double voiceMultiplicity
    ) {
        double score = founderHeroization * 0.18 + exclusionOmission * 0.18 + harmRemoval * 0.18 + commemorationSaturation * 0.14 + reputationalBranding * 0.16 + (1.0 - voiceMultiplicity) * 0.16;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(legitimacyAlignment(0.84, 0.66, 0.78, 0.82, 0.70, 0.76));
        System.out.println(originMythRisk(0.92, 0.84, 0.78, 0.90, 0.82, 0.34));
    }
}
