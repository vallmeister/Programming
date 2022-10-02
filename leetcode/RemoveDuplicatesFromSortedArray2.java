package Coding.LeetCode;

import java.util.Arrays;

public class RemoveDuplicatesFromSortedArray2 {

  public static void main(String[] args) {
    int[] nums = {1,1,1,2,2,3};
    System.out.println(removeDuplicates(nums));
    System.out.println(Arrays.toString(nums));

    nums = new int[]{1,1,1,1,2,2,2,3,4,4};
    System.out.println(removeDuplicates(nums));
    System.out.println(Arrays.toString(nums));

    nums = new int[]{0,0,1,1,1,1,2,3,3};
    System.out.println(removeDuplicates(nums));
    System.out.println(Arrays.toString(nums));
  }

  public static int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;
    int elements = 1;
    int lastNumber = nums[0];
    int numberCount = 1;
    int nextIndex = 1;

    for (int i = 1; i < nums.length; i++) {
      int number = nums[i];
      if (number == lastNumber) numberCount++;
      else if (number > lastNumber) {
        numberCount = 1;
        lastNumber = number;
      }

      if (numberCount <= 2) {
        elements++;
        nums[nextIndex] = nums[i];
        nextIndex++;
      }
    }

    return elements;
  }
}
