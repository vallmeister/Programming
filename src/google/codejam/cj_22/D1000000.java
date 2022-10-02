package Coding.codeJam.cj22;

import java.util.PriorityQueue;
import java.util.Scanner;

public class D1000000 {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int testcases = scanner.nextInt();

    for (int testcase = 1; testcase <= testcases; testcase++) {
      int number = scanner.nextInt();
      PriorityQueue<Integer> dices = new PriorityQueue<>(number);
      for (int i = 0; i < number; i++) {
        dices.add(scanner.nextInt());
      }
      int solution = 0;
      while (!dices.isEmpty()) {
        int nextDice = dices.poll();
        if (nextDice > solution) solution++;
      }

      System.out.printf("Case #%d: %d\n", testcase, solution);
    }
  }
}
