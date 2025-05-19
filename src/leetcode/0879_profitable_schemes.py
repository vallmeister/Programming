from functools import cache
from typing import List


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        m = len(profit)
        mod = 10 ** 9 + 7

        @cache
        def memo(i, target_profit, members):
            if members < 0:
                return 0
            elif i >= m:
                if target_profit <= 0:
                    return 1
                else:
                    return 0
            return (memo(i + 1, target_profit, members) + memo(i + 1, max(0, target_profit - profit[i]),
                                                               members - group[i])) % mod

        return memo(0, minProfit, n)


s = Solution()
print(s.profitableSchemes(n=5, minProfit=3, group=[2, 2], profit=[2, 3]))
print(s.profitableSchemes(n=10, minProfit=5, group=[2, 3, 5], profit=[6, 7, 8]))
