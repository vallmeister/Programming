from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total_ones = sum(nums)
        nums *= 2
        curr_ones = sum(nums[:total_ones])
        min_swaps = total_ones - curr_ones
        for right in range(total_ones, 2 * n):
            curr_ones += nums[right]
            curr_ones -= nums[right - total_ones]
            min_swaps = min(min_swaps, total_ones - curr_ones)
        return min_swaps


s = Solution()
print(s.minSwaps([0, 1, 0, 1, 1, 0, 0]))
print(s.minSwaps([0, 1, 1, 1, 0, 0, 1, 1, 0]))
print(s.minSwaps([1, 1, 0, 0, 1]))
print(s.minSwaps([0, 0, 0]))
