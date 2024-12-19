from heapq import heappush, heappop
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i, num in enumerate(nums):
            heappush(heap, (num, i))
        for _ in range(k):
            num, i = heappop(heap)
            num *= multiplier
            heappush(heap, (num, i))
        for num, i in heap:
            nums[i] = num
        return nums
