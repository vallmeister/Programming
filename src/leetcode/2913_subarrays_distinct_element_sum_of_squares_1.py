from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            elements = set()
            for j in range(i, n):
                elements.add(nums[j])
                ans += len(elements) ** 2
        return ans
