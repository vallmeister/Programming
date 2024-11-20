import math
from heapq import heappush, heappop
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans = math.inf
        n = len(nums)
        heap = [(0, -1)]
        ps = 0
        for i in range(n):
            ps += nums[i]
            while heap and ps - heap[0][0] >= k:
                _, j = heappop(heap)
                ans = min(ans, i - j)
            heappush(heap, (ps, i))

        return -1 if ans == math.inf else ans
