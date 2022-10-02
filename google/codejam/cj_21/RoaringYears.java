package Coding.codeJam.cj21;

import java.util.Scanner;

public class RoaringYears {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int testcases = scanner.nextInt();

        for (int testcase = 1; testcase <= testcases; testcase++) {
            int year = scanner.nextInt();
            int solution = 0;



            System.out.format("Case #%d: %d\n", testcase, solution);
        }
    }

    private static boolean isRoaring(int number) {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append(number);
        return false;
    }
}
