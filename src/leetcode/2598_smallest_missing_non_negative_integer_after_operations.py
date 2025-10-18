from collections import defaultdict
from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        residuals = defaultdict(int)
        for num in nums:
            residuals[num % value] += 1
        ans = 0
        while residuals[ans % value]:
            residuals[ans % value] -= 1
            ans += 1
        return ans


s = Solution()
print(s.findSmallestInteger(nums=[1, -10, 7, 13, 6, 8], value=5))
print(s.findSmallestInteger(nums=[1, -10, 7, 13, 6, 8], value=7))
