public class IndigenousStoryGovernanceCanvasScore {
    public static double relationalAccountability(
        double placeSpecificity,
        double communityAuthority,
        double tellerRelationship,
        double listenerContext,
        double obligationVisibility,
        double governanceVisibility
    ) {
        return (placeSpecificity + communityAuthority + tellerRelationship + listenerContext + obligationVisibility + governanceVisibility) / 6.0;
    }

    public static double protocolRisk(
        double accessPressure,
        double seasonalRestriction,
        double ceremonialRestriction,
        double templateForcing,
        double digitalExposure,
        double governanceVisibility
    ) {
        double score = accessPressure * 0.18 + seasonalRestriction * 0.16 + ceremonialRestriction * 0.18 + templateForcing * 0.16 + digitalExposure * 0.16 + (1.0 - governanceVisibility) * 0.16;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(relationalAccountability(0.94, 0.86, 0.82, 0.78, 0.88, 0.84));
        System.out.println(protocolRisk(0.86, 0.64, 0.78, 0.62, 0.92, 0.50));
    }
}
