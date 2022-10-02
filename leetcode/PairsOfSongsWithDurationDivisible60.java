package Coding.LeetCode;

public class PairsOfSongsWithDurationDivisible60 {
  public static void main(String[] args) {
    int[] songs = {30, 20, 150, 100, 40};
    System.out.println(numPairsDivisibleBy60(songs));
  }

  public static int numPairsDivisibleBy60(int[] time) {
    if (time.length == 1) return 0;

    int[] durations = new int[60];
    for (int i = 0; i < time.length; i++) {
      int duration = time[i] % 60;
      durations[duration]++;
    }
    int pairs = 0;
    pairs += durations[0] * (durations[0] - 1) / 2;
    pairs += durations[30] * (durations[30] - 1) / 2;
    for (int i = 1; i < 30; i++) pairs += durations[i] * durations[60 - i];

    return pairs;
  }
}
