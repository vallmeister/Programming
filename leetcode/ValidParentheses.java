package Coding.LeetCode;

import java.util.HashSet;
import java.util.Set;
import java.util.Stack;

public class ValidParentheses {

    public static void main(String[] args) {
        String s1 = "()";
        System.out.println(isValid(s1));

        String s2 = "()[]{}";
        System.out.println(isValid(s2));

        String s3 = "(]";
        System.out.println(isValid(s3));

        String s4 = "([)]";
        System.out.println(isValid(s4));

        String s5 = "{[]}";
        System.out.println(isValid(s5));
    }

    /*
    My own idea.
    Using a stack for the opening brackets and retrieve them when the according closing bracket occurs. s is invalid
    if there's the wrong bracket on the stack or the stack isn't empty afterwards and valid otherwise
     */
    public static boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        Set<Character> openingBrackets = new HashSet<>();
        openingBrackets.add('(');
        openingBrackets.add('[');
        openingBrackets.add('{');

        Set<Character> closingBrackets = new HashSet<>();
        closingBrackets.add(')');
        closingBrackets.add(']');
        closingBrackets.add('}');

        for (int i = 0; i < s.length(); i++) {
            char character = s.charAt(i);

            if (openingBrackets.contains(character)) stack.push(character);
            else if (closingBrackets.contains(character)) {
                if (stack.empty()) return false;

                char last = stack.pop();
                if (character == ')' && (last == '[' || last == '{')) return false;
                else if (character == ']' && (last == '(' || last == '{')) return false;
                else if (character == '}' && (last == '[' || last == '(')) return false;
            }
        }

        return stack.empty();
    }
}
