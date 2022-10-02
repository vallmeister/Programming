package Coding.LeetCode;

public class AddBinary {

  public static void main(String[] args) {
    System.out.println(addBinary("111", "11"));
  }

  public static String addBinary(String a, String b) {
    StringBuilder result = new StringBuilder();
    int first = a.length() - 1;
    int second = b.length() - 1;
    int carry = 0;

    while (first >= 0 || second >= 0) {
      int s1 = first < 0 ? 0 : a.charAt(first--) - '0';
      int s2 = second < 0 ? 0 : b.charAt(second--) - '0';

      int sum = s1 ^ s2 ^ carry;
      result.append(sum);
      carry = s1 & s2 | s1 & carry | s2 & carry;
    }
    if (carry == 1) result.append(1);
    return result.reverse().toString();
  }
}
