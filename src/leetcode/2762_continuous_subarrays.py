from heapq import heappush, heappop
from typing import List


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        min_heap = []
        max_heap = []
        ans = 0
        for right in range(n):
            heappush(min_heap, (nums[right], right))
            heappush(max_heap, (-nums[right], right))
            while -max_heap[0][0] - min_heap[0][0] > 2:
                left += 1
                while min_heap[0][1] < left:
                    heappop(min_heap)
                while max_heap[0][1] < left:
                    heappop(max_heap)
            ans += right - left + 1
        return ans


s = Solution()
print(s.continuousSubarrays([5, 4, 2, 4]))
