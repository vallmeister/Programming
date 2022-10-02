package Coding.LeetCode;

import java.util.Arrays;

public class RemoveDuplicatesFromSortedArray {

  public static void main(String[] args) {
    int[] num1 = {1,1,2};
    int[] num2 = {};
    int[] num3 = {0,0,1,1,1,2,2,3,3,4};

    System.out.println(removeDuplicates(num1) + " " + Arrays.toString(num1));
    System.out.println(removeDuplicates(num2) + " " + Arrays.toString(num2));
    System.out.println(removeDuplicates(num3) + " " + Arrays.toString(num3));

  }

  public static int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;

    int lastDigit = nums[0];
    int k = 1;

    for (int i = 0; i < nums.length; i++) {
      int tmp = nums[i];
      if (lastDigit < tmp) {
        nums[k] = tmp;
        k++;
        lastDigit = tmp;
      }

    }
    return k;
  }
}
