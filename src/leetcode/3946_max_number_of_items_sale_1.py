from functools import cache
from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        min_price = min(price for _, price in items)
        freebies = [1] * n
        for i, (fi, pi) in enumerate(items):
            for j, (fj, pj) in enumerate(items):
                if i == j:
                    continue
                elif fj % fi == 0:
                    freebies[i] += 1

        @cache
        def memo(idx, total):
            if idx >= n:
                return total // min_price
            f, p = items[idx]
            take = 0
            if total >= p:
                take = freebies[idx] + memo(idx + 1, total - p)
            no_take = memo(idx + 1, total)
            return max(take, no_take)

        ans = memo(0, budget)
        memo.cache_clear()
        return ans
