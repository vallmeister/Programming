package leetcode;

import java.util.HashMap;
import java.util.Map;

public class SubarraysWithAtMostKdifferentIntegers {
    public static void main(String[] args) {
        final Solution s = new Solution();
        System.out.println(s.subarraysWithKDistinct(new int[]{1, 2, 1, 2, 3}, 2));
        System.out.println(s.subarraysWithKDistinct(new int[]{1, 2, 1, 3, 4}, 3));
    }

    private static class Solution {
        public int subarraysWithKDistinct(int[] nums, int k) {
            return subarraysWithAtMostKdistinct(nums, k) - subarraysWithAtMostKdistinct(nums, k - 1);
        }

        private int subarraysWithAtMostKdistinct(int[] nums, int k) {
            final Map<Integer, Integer> frequencies = new HashMap<>();
            int left = 0;
            int count = 0;
            for (int right = 0; right < nums.length; right++) {
                int right_num = nums[right];
                int freq = frequencies.getOrDefault(right_num, 0);
                frequencies.put(right_num, ++freq);
                while (frequencies.size() > k) {
                    freq = frequencies.get(nums[left]);
                    frequencies.put(nums[left], --freq);
                    if (frequencies.get(nums[left]) == 0) {
                        frequencies.remove(nums[left]);
                    }
                    left++;
                }
                count += right - left + 1;
            }
            return count;
        }
    }
}
