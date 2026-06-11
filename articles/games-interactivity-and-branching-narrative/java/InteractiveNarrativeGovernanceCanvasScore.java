public class InteractiveNarrativeGovernanceCanvasScore {
    public static double agencyIntegrity(
        double choiceMeaningfulness,
        double systemResponse,
        double feedbackClarity,
        double roleVariation,
        double worldMemory,
        double ethicalGovernance
    ) {
        return (choiceMeaningfulness + systemResponse + feedbackClarity + roleVariation + worldMemory + ethicalGovernance) / 6.0;
    }

    public static double branchingBurden(
        double branchCountPressure,
        double stateDependency,
        double consequenceTracking,
        double testingLoad,
        double localizationCost,
        double recombinationCoherence
    ) {
        double score = branchCountPressure * 0.16 + stateDependency * 0.18 + consequenceTracking * 0.20 + testingLoad * 0.18 + localizationCost * 0.12 + (1.0 - recombinationCoherence) * 0.16;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(agencyIntegrity(0.78, 0.76, 0.74, 0.72, 0.70, 0.68));
        System.out.println(branchingBurden(0.58, 0.62, 0.66, 0.70, 0.52, 0.74));
    }
}
