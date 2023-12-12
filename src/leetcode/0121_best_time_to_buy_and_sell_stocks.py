from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_so_far = 0
        min_price = prices[0]
        for price in prices[1:]:
            profit_so_far = max(profit_so_far, price - min_price)
            min_price = min(min_price, price)
        return profit_so_far


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([7, 6, 4, 3, 1]))
