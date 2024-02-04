from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        h = {0: -1}
        count = 0
        for i in range(n):
            count -= 2 * (0.5 - nums[i])
            if count in h:
                ans = max(ans, i - h[count])
            else:
                h[count] = i
        return ans
