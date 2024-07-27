from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = sum(1 if pos % 2 == 0 else 0 for pos in position)
        odd = sum(1 if pos % 2 == 1 else 0 for pos in position)
        return min(even, odd)
