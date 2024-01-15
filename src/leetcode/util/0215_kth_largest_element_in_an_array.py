from heapq import heappush, heappop
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, num)
            while len(heap) > k:
                heappop(heap)
        return heappop(heap)


s = Solution()
print(s.findKthLargest([3, 2, 1, 5, 6, 4], k=2))
print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
