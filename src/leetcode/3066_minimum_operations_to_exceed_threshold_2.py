from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ops = 0
        heapify(nums)
        while nums[0] < k:
            x = heappop(nums)
            y = heappop(nums)
            heappush(nums, min(x, y) * 2 + max(x, y))
            ops += 1
        return ops


s = Solution()
print(s.minOperations([2, 11, 10, 1, 3], 10))
print(s.minOperations([1, 1, 2, 4, 9], 20))
