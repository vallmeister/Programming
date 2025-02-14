from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        prev = curr_sum = ans = nums[0]
        for num in nums[1:]:
            if num > prev:
                curr_sum += num
            else:
                curr_sum = num
            ans = max(ans, curr_sum)
            prev = num
        return ans
