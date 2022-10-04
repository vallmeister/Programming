package Programming.uva_judge;

import java.util.Scanner;

public class RelationalOperator_11172 {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();

    for (int test = 1; test <= t; test++) {
      int a = sc.nextInt();
      int b = sc.nextInt();

      if (a > b) System.out.println("<");
      else if (a < b) System.out.println(">");
      else System.out.println("=");
    }
  }
}
