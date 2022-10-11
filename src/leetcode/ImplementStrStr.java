package Programming.leetcode;

public class ImplementStrStr {

  public static void main(String[] args) {
    System.out.println(intstrStr("hello", "ll"));
    System.out.println(intstrStr("aaaaa", "bba"));
    System.out.println(intstrStr("", "needle"));
    System.out.println(intstrStr("", ""));
    System.out.println(intstrStr("mississippi", "issip"));
    System.out.println(intstrStr("mississippi", "issipi"));
  }

  public static int intstrStr(String haystack, String needle) {
    if (needle.equals("") || needle.equals(haystack)) return 0;
    else if (haystack.length() < needle.length()) return -1;

    char start = needle.charAt(0);
    HAYSTACK: for (int i = 0; i <= haystack.length() - needle.length(); i++) {
      if (start == haystack.charAt(i)) {
        for (int j = i + 1; j < i + needle.length() && j < haystack.length(); j++) {
          if (haystack.charAt(j) != needle.charAt(j - i)) continue HAYSTACK;
        }
        return i;
      }
    }
    return -1;
  }
}
