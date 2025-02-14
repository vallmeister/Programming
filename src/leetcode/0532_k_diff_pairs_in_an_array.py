from collections import Counter
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            return sum(1 if val >= 2 else 0 for val in Counter(nums).values())
        num_set = set()
        pairs = 0
        for num in nums:
            if num in num_set:
                continue
            if num + k in num_set:
                pairs += 1
            if num - k in num_set:
                pairs += 1
            num_set.add(num)
        return pairs
