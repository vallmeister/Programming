from functools import cache
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        c = len(coins)

        @cache
        def memo(left_amount, start):
            if left_amount < 0:
                return 0
            elif left_amount == 0:
                return 1
            res = 0
            for i in range(start, c):
                res += memo(left_amount - coins[i], i)
            return res

        return memo(amount, 0)


s = Solution()
print(s.change(5, [1, 2, 5]))
