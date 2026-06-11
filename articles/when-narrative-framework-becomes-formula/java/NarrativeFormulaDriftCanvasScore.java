public class NarrativeFormulaDriftCanvasScore {
    public static double formulaDrift(double templateForcing, double beatRigidity, double closurePressure, double universalityPressure, double automationDependence, double storySpecificity) {
        double score = templateForcing * 0.20 + beatRigidity * 0.18 + closurePressure * 0.18 + universalityPressure * 0.16 + automationDependence * 0.14 + (1.0 - storySpecificity) * 0.14;
        return Math.min(1.0, score);
    }
    public static void main(String[] args) {
        System.out.println(formulaDrift(0.90, 0.82, 0.88, 0.74, 0.94, 0.36));
    }
}
