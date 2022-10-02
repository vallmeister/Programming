package Coding.codeJam.cj22;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class PancakeDeque {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int testcases = scanner.nextInt();

        for (int testcase = 1; testcase <= testcases; testcase++) {
            int number = scanner.nextInt();
            Deque<Integer> pancakes = new ArrayDeque<>(number);
            for (int j = 0; j < number; j++) {
                pancakes.add(scanner.nextInt());
            }

            int customers = 0;
            int minimumDeliciousness = 0;

            while (!pancakes.isEmpty()) {
                int first = pancakes.peekFirst();
                int last = pancakes.peekLast();

                if (first < minimumDeliciousness) {
                    pancakes.removeFirst();
                    continue;
                }
                if (last < minimumDeliciousness) {
                    pancakes.removeLast();
                    continue;
                }

                if (first < last) minimumDeliciousness = pancakes.removeFirst();
                else minimumDeliciousness = pancakes.removeLast();
                customers++;
            }

            System.out.format("Case #%d: %d\n", testcase, customers);
        }
    }
}
