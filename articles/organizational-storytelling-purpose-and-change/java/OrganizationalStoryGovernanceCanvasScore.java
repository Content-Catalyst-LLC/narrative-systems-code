public class OrganizationalStoryGovernanceCanvasScore {
    public static double purposeAlignment(
        double missionClarity,
        double decisionAlignment,
        double budgetFit,
        double stakeholderImpact,
        double employeeExperience,
        double governanceTransparency
    ) {
        return (missionClarity + decisionAlignment + budgetFit + stakeholderImpact + employeeExperience + governanceTransparency) / 6.0;
    }

    public static double narrativeExtractionRisk(
        double consentDeficit,
        double selectionBias,
        double powerAsymmetry,
        double emotionalTargeting,
        double brandRepurposing,
        double agency
    ) {
        double score = consentDeficit * 0.18 + selectionBias * 0.16 + powerAsymmetry * 0.18 + emotionalTargeting * 0.16 + brandRepurposing * 0.16 + (1.0 - agency) * 0.16;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(purposeAlignment(0.82, 0.66, 0.58, 0.70, 0.52, 0.54));
        System.out.println(narrativeExtractionRisk(0.56, 0.72, 0.70, 0.64, 0.78, 0.44));
    }
}
