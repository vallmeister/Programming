from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = [0] * 32
        for num in nums:
            for i in range(32):
                bits[i] += num & 1
                num >>= 1
        for i in range(32):
            bits[i] %= 3
        ans = 0
        for i in range(32):
            ans += bits[i] * 2 ** i
        if ans > 2 ** 31 - 1:
            ans -= 2 ** 32
        return ans


s = Solution()
print(s.singleNumber([2, 2, 3, 2, -1, -1, -1]))
print(s.singleNumber([0, 1, 0, 1, 0, 1, 99]))
print(s.singleNumber([-2, -2, 1, 1, 4, 1, 4, 4, -4, -2]))
