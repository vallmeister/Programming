import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.ps = []
        self.total = 0
        for weight in w:
            self.total += weight
            self.ps.append(self.total)

    def pickIndex(self) -> int:
        target = random.random() * self.total
        left, right = 0, len(self.ps) - 1
        while left < right:
            mid = (left + right) // 2
            if target > self.ps[mid]:
                left = mid + 1
            else:
                right = mid
        return left

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
