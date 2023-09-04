from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                sign *= -1
        return sign


s = Solution()
print(s.arraySign([-1, -2, -3, -4, 3, 2, 1]))
print(s.arraySign([1, 5, 0, 2, -3]))
print(s.arraySign([-1, 1, -1, 1, -1]))
