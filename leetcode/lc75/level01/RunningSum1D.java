package Coding.LeetCode.lc75.level01;

import java.util.Arrays;

public class RunningSum1D {

    public static void main(String[] args) {
        int[] example01 = new int[]{1,2,3,4};
        int[] example02 = new int[]{1,1,1,1,1};
        int[] example03 = new int[]{3,1,2,10,1};

        System.out.println(Arrays.toString(runningSum(example01)));
        System.out.println(Arrays.toString(runningSum(example02)));
        System.out.println(Arrays.toString(runningSum(example03)));
    }

    public static int[] runningSum(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            nums[i] = nums[i-1] + nums[i];
        }
        return nums;
    }
}
