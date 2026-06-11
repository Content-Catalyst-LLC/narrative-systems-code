public class SacredHistoryCanvasScore {
    public static double revelatoryClaimStrength(double disclosure, double eventMeaning, double authorityClarity, double obligation, double transformation, double communalMemory) {
        return (disclosure + eventMeaning + authorityClarity + obligation + transformation + communalMemory) / 6.0;
    }
    public static void main(String[] args) {
        System.out.println(revelatoryClaimStrength(0.94, 0.92, 0.84, 0.78, 0.82, 0.88));
    }
}
