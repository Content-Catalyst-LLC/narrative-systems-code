public class NonHeroicNarrativeCanvasScore {
    public static double tragicStructure(
        double consequentialAction,
        double limitPressure,
        double reversal,
        double recognitionKnowledge,
        double irreversibility,
        double witnessBurden
    ) {
        return (consequentialAction + limitPressure + reversal + recognitionKnowledge + irreversibility + witnessBurden) / 6.0;
    }

    public static double nonHeroicAgency(
        double care,
        double endurance,
        double witness,
        double refusal,
        double maintenance,
        double survival
    ) {
        return (care + endurance + witness + refusal + maintenance + survival) / 6.0;
    }

    public static void main(String[] args) {
        System.out.println(tragicStructure(0.88, 0.86, 0.78, 0.84, 0.88, 0.82));
        System.out.println(nonHeroicAgency(0.94, 0.90, 0.74, 0.62, 0.92, 0.88));
    }
}
