class Solution:
    # TODO: Revise
    def maxProfit(self, prices: list[int]) -> int:
        prev = prices[0]
        last_price = prev
        profit = 0
        curr_profit = 0
        for price in prices[1:]:
            if price < last_price:
                prev = price
                profit += curr_profit
                curr_profit = 0
            else:
                curr_profit = price - prev
            last_price = price
        profit += curr_profit
        return profit


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([1, 2, 3, 4, 5]))
print(s.maxProfit([7, 6, 4, 3, 1]))
