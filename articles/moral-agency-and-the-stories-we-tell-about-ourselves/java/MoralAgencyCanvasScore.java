public class MoralAgencyCanvasScore {
    public static double moralClarity(
        double actionNaming,
        double intentionDistinction,
        double consequenceClarity,
        double harmMarking,
        double repairOrientation,
        double otherVisibility
    ) {
        return (actionNaming + intentionDistinction + consequenceClarity + harmMarking + repairOrientation + otherVisibility) / 6.0;
    }

    public static double excuseRisk(
        double contextOveruse,
        double intentionShielding,
        double victimhoodShielding,
        double blameShifting,
        double growthSubstitution,
        double harmMinimization
    ) {
        double score = contextOveruse * 0.16 + intentionShielding * 0.18 + victimhoodShielding * 0.18 + blameShifting * 0.18 + growthSubstitution * 0.16 + harmMinimization * 0.14;
        return Math.min(1.0, score);
    }

    public static void main(String[] args) {
        System.out.println(moralClarity(0.86, 0.82, 0.84, 0.88, 0.80, 0.82));
        System.out.println(excuseRisk(0.36, 0.42, 0.30, 0.34, 0.40, 0.32));
    }
}
