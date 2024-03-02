from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        ops = 0
        while nums[0] < k:
            mn = heappop(nums)
            mx = heappop(nums)
            heappush(nums, mn * 2 + mx)
            ops += 1
        return ops


s = Solution()
print(s.minOperations([2, 11, 10, 1, 3], k=10))
print(s.minOperations([1, 1, 2, 4, 9], k=20))
