import math
from typing import List


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        cache = [[[-1] * 3 for _ in range(k + 1)] for _ in range(n)]

        # state 0: no transaction is ongoing
        # state 1: we bought the stock and wait for sale
        # state 2: we short-sold the stock and wait to rebuy it
        def memo(i, k_left, state):
            if k_left < 0:
                return -math.inf
            elif i >= n:
                return 0 if state == 0 else -math.inf
            elif cache[i][k_left][state] != -1:
                return cache[i][k_left][state]
            no_transaction = memo(i + 1, k_left, state)
            normal_transaction = -math.inf
            short_transaction = -math.inf
            match state:
                case 0:
                    normal_transaction = -prices[i] + memo(i + 1, k_left - 1, 1)
                    short_transaction = prices[i] + memo(i + 1, k_left - 1, 2)
                case 1:
                    normal_transaction = prices[i] + memo(i + 1, k_left, 0)
                case 2:
                    short_transaction = -prices[i] + memo(i + 1, k_left, 0)
            cache[i][k_left][state] = max(no_transaction, normal_transaction, short_transaction)
            return cache[i][k_left][state]

        memo(0, k, 0)
        return cache[0][k][0]


s = Solution()
print(s.maximumProfit(prices=[1, 7, 9, 8, 2], k=2))
