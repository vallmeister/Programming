package Coding.LeetCode.lc75.level01;

import java.util.Arrays;

public class FindPivotIndex {

    public static void main(String[] args) {
        int[] example01 = new int[]{1,7,3,6,5,6};
        int[] example02 = new int[]{1,2,3};
        int[] example03 = new int[]{2,1,-1};

        System.out.println(pivotIndexFast(example01));
        System.out.println(pivotIndexFast(example02));
        System.out.println(pivotIndexFast(example03));
    }

    public static int pivotIndex(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int leftSum = 0;
            for (int j = 0; j < i; j++) leftSum += nums[j];
            int rightSum = 0;
            for (int j = i + 1; j < nums.length; j++) rightSum += nums[j];

            if (leftSum == rightSum) return i;
        }

        return -1;
    }

    public static int pivotIndexFast(int[] nums) {
        int leftSum = 0;
        int rightSum = Arrays.stream(nums).sum();
        rightSum -= nums[0];

        for (int i = 0; i < nums.length; i++) {
            if (i > 0) {
                leftSum += nums[i-1];
                rightSum -= nums[i];
            }
            if (rightSum == leftSum) return i;
        }
        return -1;
    }
}
