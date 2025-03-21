from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i] == 1:
                continue
            elif i > n - 3:
                return -1
            for j in range(i, i + 3):
                nums[j] = 1 - nums[j]
            ans += 1
        return ans
