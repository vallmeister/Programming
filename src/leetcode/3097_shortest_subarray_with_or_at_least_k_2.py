import math
from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1
        ans = math.inf
        bits = [0] * 32
        left = 0
        for right in range(len(nums)):
            for i in range(32):
                if nums[right] & (1 << i) > 0:
                    bits[i] += 1
            while self.bits_geq_k(bits, k):
                ans = min(ans, right - left + 1)
                for i in range(32):
                    if nums[left] & (1 << i) > 0:
                        bits[i] -= 1
                left += 1
        return ans if ans < math.inf else -1

    def bits_geq_k(self, bits, k):
        num = 0
        for i in range(32):
            if bits[i] > 0:
                num |= (1 << i)
        return num >= k
