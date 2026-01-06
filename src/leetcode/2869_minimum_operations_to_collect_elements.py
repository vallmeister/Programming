from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        elements = 0
        for i in range(1, k + 1):
            elements |= 1 << i
        ans = 0
        while elements:
            num = nums.pop()
            mask = 1 << num
            if elements & mask:
                elements ^= mask
            ans += 1
        return ans
