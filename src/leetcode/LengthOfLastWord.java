package Coding.LeetCode;

public class LengthOfLastWord {

  public static int lengthOfLastWord(String s) {
    String[] strings = s.split(" ");
    return strings[strings.length - 1].length();
  }
}
