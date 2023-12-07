from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_sum = -1
        nums.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            curr_sum = nums[i] + nums[j]
            if curr_sum < k:
                max_sum = max(max_sum, curr_sum)
                i += 1
            else:
                j -= 1
        return max_sum


s = Solution()
print(s.twoSumLessThanK([34, 23, 1, 24, 75, 33, 54, 8], k=60))
print(s.twoSumLessThanK([10, 20, 30], k=15))
