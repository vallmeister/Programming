package Programming.leetcode;

public class BreakAPalindrome_1328 {

  public String breakPalindrome(String palindrome) {
    if (palindrome.length() == 1) return "";
    char[] chars = palindrome.toCharArray();
    for (int i = 0; i < chars.length / 2; i++) {
      if (chars[i] > 'a') {
        chars[i] = 'a';
        return String.valueOf(chars);
      }
    }
    for (int i = chars.length - 1; i >= chars.length / 2; i--) {
      if (chars[i] == 'a') {
        chars[i] = 'b';
        return String.valueOf(chars);
      }
    }
    return "";
  }
}
