import math
from heapq import heappush
from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        residual_classes = [[] for _ in range(k)]
        heappush(residual_classes[0], 0)
        ps = 0
        ans = -math.inf
        for i, num in enumerate(nums):
            ps += num
            r = (i + 1) % k
            if residual_classes[r]:
                ans = max(ans, ps - residual_classes[r][0])
            heappush(residual_classes[r], ps)
        return ans


s = Solution()
print(s.maxSubarraySum(nums=[1, 2], k=1))
print(s.maxSubarraySum(nums=[-1, -2, -3, -4, -5], k=4))
print(s.maxSubarraySum(nums=[-5, 1, 2, -3, 4], k=2))
