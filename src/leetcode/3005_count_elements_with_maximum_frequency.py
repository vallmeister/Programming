from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_frequency = max(counter.values())
        return sum(val for val in counter.values() if val == max_frequency)
