package Coding.codeJam.cj22;

import java.util.Scanner;

public class PunchedCards {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int testcases = scanner.nextInt();

    for (int test = 1; test <= testcases; test++) {
      int r = scanner.nextInt();
      int c = scanner.nextInt();

      int rows = 2 * r + 1;
      int columns = 2 * c + 1;
      char[][] solution = new char[rows][columns];

      for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
          if (i < 2 && j < 2) {
            solution[i][j] = '.';
            continue;
          }
          if (i % 2 == 0) {
            if (j % 2 == 0) solution[i][j] = '+';
            else solution[i][j] = '-';
          } else {
            if (j % 2 == 0) solution[i][j] = '|';
            else solution[i][j] = '.';
          }
        }
      }
      System.out.format("Case #%d:\n", test);
      for (int j = 0; j < rows; j++) System.out.println(new String(solution[j]));
    }
  }
}
