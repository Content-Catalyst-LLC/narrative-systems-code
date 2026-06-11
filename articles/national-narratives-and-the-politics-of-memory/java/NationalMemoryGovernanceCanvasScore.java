public class NationalMemoryGovernanceCanvasScore {
    public static double memoryPlurality(
        double groupRepresentation,
        double sourceDiversity,
        double testimonyVisibility,
        double archiveCoverage,
        double countermemoryInclusion,
        double dissentSpace
    ) {
        return (groupRepresentation + sourceDiversity + testimonyVisibility + archiveCoverage + countermemoryInclusion + dissentSpace) / 6.0;
    }

    public static double nationalMythRisk(
        double heroCompression,
        double innocenceStory,
        double exclusionOmission,
        double victimhoodMonopoly,
        double puritySymbolism,
        double revisionCapacity
    ) {
        double score = heroCompression * 0.17 + innocenceStory * 0.18 + exclusionOmission * 0.18 + victimhoodMonopoly * 0.15 + puritySymbolism * 0.14 + (1.0 - revisionCapacity) * 0.18;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(memoryPlurality(0.68, 0.72, 0.74, 0.70, 0.78, 0.72));
        System.out.println(nationalMythRisk(0.84, 0.78, 0.82, 0.66, 0.70, 0.42));
    }
}
