from collections import defaultdict
from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        ans = 0
        seen = defaultdict(int)
        n = len(nums)
        for i in range(1, n):
            curr = nums[i]
            for j in range(i):
                prev = nums[j]
                residual = (curr + prev) % k
                if (j, residual) in seen:
                    seen[(i, residual)] = max(seen[(i, residual)], seen[(j, residual)] + 1)
                else:
                    seen[(i, residual)] = 2
                ans = max(ans, seen[(i, residual)])
        return ans


s = Solution()
print(s.maximumLength(nums=[1, 2, 3, 4, 5], k=2))
print(s.maximumLength(nums=[1, 4, 2, 3, 1, 4], k=3))
