package Coding.LeetCode;

public class FindTownJudge {

  public static int findJudge(int n, int[][] trust) {
    if (n == 1) return 1;
    int[][] trustRelations = new int[n][2]; // trustRelations[i][0] person i trusts so many people

    for (int i = 0; i < trust.length; i++) {
      int trustingPerson = trust[i][0];
      int trustedPerson = trust[i][1];
      trustRelations[trustingPerson - 1][0]++;
      trustRelations[trustedPerson - 1][1]++;
    }
    for (int i = 0; i < n; i++) {
      if (trustRelations[i][0] == 0 && trustRelations[i][1] == n - 1) return i + 1;
    }
    return -1;
  }
}
