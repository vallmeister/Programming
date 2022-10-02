package Coding.LeetCode;

import java.util.*;

public class ParlindromePartitioning {

  private static Set<String> parlindromes = new HashSet<>();

  public static List<List<String>> partition(String s) {
    List<List<String>> result = new ArrayList<>();
    if (s.length() == 0) return new ArrayList<>(result);



    return new ArrayList<>(result);
  }

  private static boolean isParlindrome(String string) {
    if (parlindromes.contains(string) || string.length() == 1) return true;
    int i = 0;
    int j = string.length() - 1;
    while (i < j) {
      if (string.charAt(i) != string.charAt(j)) return false;
      i++;
      j--;
    }
    parlindromes.add(string);
    return true;
  }
}
