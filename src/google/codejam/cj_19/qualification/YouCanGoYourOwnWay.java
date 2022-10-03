package Programming.google.codejam.cj_19.qualification;

import java.util.Scanner;

public class YouCanGoYourOwnWay {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    for (int testcase = 1; testcase <= t; testcase++) {
      int n = sc.nextInt();
      String p = sc.next();
      StringBuilder sol = new StringBuilder(2 * n - 2);

      for (int i = 0; i < p.length(); i++) {
        if (p.charAt(i) == 'E') sol.append('S');
        else sol.append('E');
      }
      System.out.printf("Case #%d: %s%n", testcase, sol.toString());
    }
  }
}
