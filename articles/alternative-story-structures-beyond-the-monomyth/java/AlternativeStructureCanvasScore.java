public class AlternativeStructureCanvasScore {
    public static double structuralPlurality(
        double arcSignal,
        double cycleSignal,
        double braidSignal,
        double mosaicSignal,
        double networkSignal,
        double relationalSignal,
        double fragmentSignal
    ) {
        return (arcSignal + cycleSignal + braidSignal + mosaicSignal + networkSignal + relationalSignal + fragmentSignal) / 7.0;
    }

    public static double monomythOverfitRisk(
        double heroForcing,
        double conflictSubstitution,
        double returnPressure,
        double individualizationPressure,
        double templateForcing,
        double evidenceVisibility
    ) {
        double score = heroForcing * 0.20 + conflictSubstitution * 0.18 + returnPressure * 0.16 + individualizationPressure * 0.18 + templateForcing * 0.18 + (1.0 - evidenceVisibility) * 0.10;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(structuralPlurality(0.32, 0.50, 0.62, 0.54, 0.42, 0.92, 0.58));
        System.out.println(monomythOverfitRisk(0.78, 0.70, 0.62, 0.74, 0.80, 0.82));
    }
}
