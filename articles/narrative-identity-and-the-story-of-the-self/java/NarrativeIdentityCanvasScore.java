public class NarrativeIdentityCanvasScore {
  public static double narrativeCoherence(double memoryContinuity, double temporalProgression, double agency, double relationalGrounding, double promiseResponsibility, double futureOpenness) {
    return (memoryContinuity + temporalProgression + agency + relationalGrounding + promiseResponsibility + futureOpenness) / 6.0;
  }
  public static void main(String[] args) { System.out.println(narrativeCoherence(0.86, 0.82, 0.84, 0.78, 0.88, 0.80)); }
}
