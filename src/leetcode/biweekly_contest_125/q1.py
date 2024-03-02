from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(1 if num < k else 0 for num in nums)
