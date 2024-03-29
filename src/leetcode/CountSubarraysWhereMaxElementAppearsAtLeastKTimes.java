package leetcode;

import java.util.Arrays;

public class CountSubarraysWhereMaxElementAppearsAtLeastKTimes {
    public static void main(String[] args) {
        final Solution s = new Solution();
        System.out.println(s.countSubarrays(new int[]{1, 3, 2, 3, 3}, 2));
        System.out.println(s.countSubarrays(new int[]{1, 4, 2, 1}, 3));
    }
}

class Solution {
    public long countSubarrays(int[] nums, int k) {
        final int maxElement = Arrays.stream(nums).max().getAsInt();
        int left = 0;
        int maxCount = 0;
        long ans = 0;
        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == maxElement) maxCount++;
            while (maxCount >= k) {
                if (nums[left++] == maxElement) {
                    maxCount--;
                }
            }
            ans += left;
        }
        return ans;
    }
}
