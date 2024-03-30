package leetcode;

import java.util.ArrayList;
import java.util.List;

public class ArmstrongNumber {
    public static void main(String[] args) {
        final Solution s = new Solution();
        System.out.println(s.isArmstrong(153));
        System.out.println(s.isArmstrong(123));
    }

    static class Solution {
        public boolean isArmstrong(int n) {
            int m = n;
            final List<Integer> digits = new ArrayList<>();
            while (m > 0) {
                int digit = m % 10;
                digits.add(digit);
                m /= 10;
            }
            int sum = 0;
            for (int d: digits) {
                sum += (int) Math.pow(d, digits.size());
            }
            return sum == n;
        }
    }
}

