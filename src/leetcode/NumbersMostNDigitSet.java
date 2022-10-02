package Coding.LeetCode;

public class NumbersMostNDigitSet {

  public static void main(String[] args) {
    String[] digits = new String[]{"1", "2", "3", "6", "7", "8"};
    System.out.println(atMostNGivenDigitSet(digits, 11));
  }

  public static int atMostNGivenDigitSet(String[] digits, int n) {
    String S = String.valueOf(n);
    int K = S.length();
    int[] dp = new int[K + 1];
    dp[K] = 1;

    for (int i = K-1; i >= 0; --i) {
      int Si = S.charAt(i) - '0';
      for (String digit : digits) {
        if (Integer.parseInt(digit) < Si) {
          dp[i] += Math.pow(digits.length, K-i-1);
        } else if (Integer.parseInt(digit) == Si) {
          dp[i] += dp[i+1];
        }
      }
    }
    for (int i = 1; i < K; i++) {
      dp[0] += Math.pow(digits.length, i);
    }
    return dp[0];
  }
}
