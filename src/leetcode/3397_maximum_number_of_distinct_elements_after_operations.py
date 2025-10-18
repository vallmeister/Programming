import math
from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        prev = -math.inf
        ans = 0
        for num in nums:
            if prev >= num + k:
                continue
            ans += 1
            prev = max(prev + 1, num - k)
        return ans


s = Solution()
print(s.maxDistinctElements(nums=[1, 2, 2, 3, 3, 4], k=2))
print(s.maxDistinctElements(nums=[4, 4, 4, 4], k=1))
