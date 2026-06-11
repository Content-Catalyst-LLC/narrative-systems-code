public class MythRitualSymbolicCanvasScore {
    public static double symbolicFunction(
        double originFunction,
        double cosmologicalOrder,
        double memoryFunction,
        double identityFunction,
        double transitionFunction,
        double authorityFunction
    ) {
        return (
            originFunction +
            cosmologicalOrder +
            memoryFunction +
            identityFunction +
            transitionFunction +
            authorityFunction
        ) / 6.0;
    }

    public static double ethicalRisk(
        double totalizingOrder,
        double scapegoatingRisk,
        double exclusionRisk,
        double appropriationRisk,
        double harmExposure,
        double governanceControl
    ) {
        double risk =
            totalizingOrder * 0.18 +
            scapegoatingRisk * 0.20 +
            exclusionRisk * 0.18 +
            appropriationRisk * 0.18 +
            harmExposure * 0.16 +
            (1.0 - governanceControl) * 0.10;

        return Math.min(1.0, risk);
    }

    public static void main(String[] args) {
        System.out.println(symbolicFunction(0.94, 0.92, 0.84, 0.76, 0.70, 0.78));
        System.out.println(ethicalRisk(0.42, 0.28, 0.62, 0.94, 0.78, 0.18));
    }
}
