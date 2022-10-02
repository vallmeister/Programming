package Coding.codeJam.cj22;

import java.util.Scanner;

public class Printing3D {
  private static final String IMPOSSIBLE = " IMPOSSIBLE";

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int testcases = scanner.nextInt();

    // read input
    for (int testcase = 1; testcase <= testcases; testcase++) {
      // read input and find out what we're working with
      int minCyan = Integer.MAX_VALUE;
      int minMagenta = Integer.MAX_VALUE;
      int minYellow = Integer.MAX_VALUE;
      int minBlack = Integer.MAX_VALUE;
      int[] minInks = {minCyan, minMagenta, minYellow, minBlack};

      for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
          int temp;
          if ((temp = scanner.nextInt()) < minInks[j]) minInks[j] = temp;
        }
      }
      System.out.printf("Case #%d:", testcase);
      int sum = 0;
      for (int i = 0; i < 4; i++) sum += minInks[i];
      if (sum < 1_000_000) System.out.println(IMPOSSIBLE);
      else {
        int usedInk = 0;
        for (int i = 0; i < 4; i++) {
          int ink = Math.min(minInks[i], 1_000_000 - usedInk);
          usedInk += ink;
          System.out.print(" " + ink);
        }
        System.out.println();
      }
    }
  }
}
