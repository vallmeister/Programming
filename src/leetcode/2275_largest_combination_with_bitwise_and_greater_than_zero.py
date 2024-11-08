from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        curr_max = 0
        for i in range(32):
            curr_max = max(curr_max, sum(num & (1 << i) > 0 for num in candidates))
        return curr_max
