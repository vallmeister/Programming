package Coding.LeetCode;

public class BasicCalculator2 {
  public static void main(String[] args) {
    System.out.println(calculate("3+2*2"));
    System.out.println(calculate("3/2"));
    System.out.println(calculate("3+5/2"));
  }

  public static int calculate(String s) {
    if (s == null || s.isEmpty()) return 0;
    int length = s.length();
    int currentNumber = 0, lastNumber = 0, result = 0;
    char operation = '+';
    for (int i = 0; i < length; i++) {
      char currentChar = s.charAt(i);
      if (Character.isDigit(currentChar)) {
        currentNumber = (currentNumber * 10) + (currentChar - '0');
      }
      if (!Character.isDigit(currentChar) && !Character.isWhitespace(currentChar) || i == length - 1) {
        if (operation == '+' || operation == '-') {
          result += lastNumber;
          lastNumber = (operation == '+') ? currentNumber : -currentNumber;
        } else if (operation == '*') {
          lastNumber = lastNumber * currentNumber;
        } else if (operation == '/') {
          lastNumber = lastNumber / currentNumber;
        }
        operation = currentChar;
        currentNumber = 0;
      }
    }
    result += lastNumber;
    return result;
  }
}
