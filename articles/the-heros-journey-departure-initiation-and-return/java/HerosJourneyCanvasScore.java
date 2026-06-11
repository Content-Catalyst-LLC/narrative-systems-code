public class HerosJourneyCanvasScore {
    public static double journeyStructure(double departure, double threshold, double trial, double descent, double boon, double ret) {
        return (departure + threshold + trial + descent + boon + ret) / 6.0;
    }

    public static void main(String[] args) {
        System.out.println(journeyStructure(0.90, 0.86, 0.84, 0.74, 0.78, 0.82));
    }
}
