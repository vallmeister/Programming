from typing import List


class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        cache = [[-1] * n for _ in range(n)]

        def memo(i, k):
            if i >= n:
                return 0
            elif cache[i][k] != -1:
                return cache[i][k]
            purchase = prices[i] + memo(i + 1, i + 1)
            if k == 0:
                return purchase
            free = memo(i + 1, k - 1)
            cache[i][k] = min(purchase, free)
            return cache[i][k]

        return memo(0, 0)


s = Solution()
print(s.minimumCoins(prices=[3, 1, 2]))
print(s.minimumCoins(prices=[1, 10, 1, 1]))
print(s.minimumCoins(prices=[26, 18, 6, 12, 49, 7, 45, 45]))
