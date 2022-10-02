package Coding.LeetCode;

import java.util.Arrays;

public class RemoveElement {

  public static void main(String[] args) {
    int[] num1 = {3,2,2,3};
    int[] num2 = {};
    int[] num3 = {0,1,2,2,3,0,4,2};

    System.out.println(removeElement(num1, 3) + " " + Arrays.toString(num1));
    System.out.println(removeElement(num2, 2) + " " + Arrays.toString(num2));
    System.out.println(removeElement(num3, 2) + " " + Arrays.toString(num3));
  }

  public static int removeElement(int[] nums, int val) {
    if (nums.length == 0) return 0;
    int i = 0;

    for (int j = 0; j < nums.length; j++) {
      if (nums[j] != val) {
        nums[i] = nums[j];
        i++;
      }
    }
    return i;
  }
}
