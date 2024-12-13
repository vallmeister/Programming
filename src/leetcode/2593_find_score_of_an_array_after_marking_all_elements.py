from heapq import heappush, heappop
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        marked = set()
        heap = []
        for i, num in enumerate(nums):
            heappush(heap, (num, i))
        while heap:
            num, idx = heappop(heap)
            if idx in marked:
                continue
            marked.update([idx - 1, idx, idx + 1])
            score += num
        return score
