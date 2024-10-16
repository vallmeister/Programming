from heapq import heapify, heappop, heappush
from math import ceil
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapify(nums)
        score = 0
        for _ in range(k):
            element = heappop(nums)
            score -= element
            heappush(nums, -ceil(abs(element) / 3))
        return score
