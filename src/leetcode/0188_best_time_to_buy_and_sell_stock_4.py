from functools import cache
from typing import List


class Solution:
    # too slow
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def recursive(start, transactions):
            if transactions == 0 or start >= n:
                return 0
            profit = 0
            min_so_far = prices[start]
            for i in range(start + 1, n):
                profit = max(profit, prices[i] - min_so_far + recursive(i, transactions - 1))
                min_so_far = min(min_so_far, prices[i])
            return profit

        return recursive(0, k)


s = Solution()
print(s.maxProfit(2, [2, 4, 1]))
print(s.maxProfit(2, [3, 2, 6, 5, 0, 3]))
print(s.maxProfit(2, [3, 3, 5, 0, 0, 3, 1, 4]))
