from math import log2
from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        n = len(nums)
        bits = [0] * n
        for i in range(1, n):
            lg = int(log2(i))
            bits[i] = bits[i - 2 ** lg] + 1
        return sum(num for idx, num in enumerate(nums) if bits[idx] == k)


s = Solution()
print(s.sumIndicesWithKSetBits(nums=[5, 10, 1, 5, 2], k=1))
print(s.sumIndicesWithKSetBits(nums=[4, 3, 2, 1], k=2))
