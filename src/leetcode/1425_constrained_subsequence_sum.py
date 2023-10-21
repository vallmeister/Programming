from heapq import heappush, heappop
from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = nums[0]
        heap = []
        heappush(heap, (-nums[0], 0))
        for i in range(1, n):
            while i - heap[0][1] > k:
                heappop(heap)
            curr = max(0, -heap[0][0]) + nums[i]
            ans = max(ans, curr)
            heappush(heap, (-curr, i))
        return ans


s = Solution()
print(s.constrainedSubsetSum([10, 2, -10, 5, 20], k=2))
print(s.constrainedSubsetSum([-1, -2, -3], k=1))
print(s.constrainedSubsetSum([10, -2, -10, -5, 20], k=2))
print(s.constrainedSubsetSum([-5266, 4019, 7336, -3681, -5767], 2))
