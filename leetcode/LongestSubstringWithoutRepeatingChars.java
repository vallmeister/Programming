package Coding.LeetCode;

public class LongestSubstringWithoutRepeatingChars {

  public static void main(String[] args) {
    System.out.println(lengthOfLongestSubstring("abcabcbb"));
    System.out.println(lengthOfLongestSubstring("bbbbb"));
    System.out.println(lengthOfLongestSubstring("pwwkew"));
    System.out.println(lengthOfLongestSubstring(""));
    System.out.println(lengthOfLongestSubstring("qrsvbspk"));
  }

  public static int lengthOfLongestSubstring(String s) {
    int[] chars = new int[128]; // all ASCII characters
    int left = 0;
    int right = 0;
    int result = 0;

    while (right < s.length()) {
      char r = s.charAt(right);
      chars[r]++;

      while (chars[r] > 1) {
        char l = s.charAt(left);
        chars[l]--;
        left++;
      }
      result = Math.max(result, right - left + 1);
      right++;
    }
    return result;
  }
}
