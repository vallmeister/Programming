package Coding.codeJam.cj22;

import java.util.*;

public class DoubleOrOneThing {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int testcases = scanner.nextInt();

        for (int testcase = 1; testcase <= testcases; testcase++) {
            String input = scanner.next();
            System.out.format("Case #%d: %s\n", testcase, solve(input));
        }
    }

    private static String solve(String string) {
        int stringLength = string.length();
        if (stringLength == 1) return string;

        StringBuilder stringBuilder = new StringBuilder();
        List<Character> characters = new ArrayList<>();
        List<Integer> repetitions = new ArrayList<>();

        characters.add(string.charAt(0));
        int count = 1;
        for (int i = 1; i < stringLength; i++) {
            if (string.charAt(i) == string.charAt(i - 1)) count++;
            else {
                repetitions.add(count);
                characters.add(string.charAt(i));
                count = 1;
            }
        }
        repetitions.add(count);

        int size = characters.size();
        for (int i = 0; i < size - 1; i++) {
            char current = characters.get(i);
            if (current < characters.get(i + 1)) {
                for (int j = 0; j < repetitions.get(i) * 2; j++) stringBuilder.append(current);
            } else {
                for (int j = 0; j < repetitions.get(i); j++) stringBuilder.append(current);
            }
        }
        char last = characters.get(size - 1);
        for (int i = 0; i < repetitions.get(size - 1); i++) {
            stringBuilder.append(last);
        }
        return stringBuilder.toString();
    }
}
