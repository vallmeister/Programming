class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n = len(prices)
        curr_sell = prices[n - 1] - fee
        curr_buy = 0
        for i in range(n - 2, -1, -1):
            curr_sell = max(curr_sell, curr_buy + prices[i] - fee)
            curr_buy = max(curr_buy, curr_sell - prices[i])
        return curr_buy

    def max_profit_dp(self, prices: list[int], fee: int) -> int:
        n = len(prices)
        dp = [
            [0] * (n + 1),  # Sell
            [0] * (n + 1)  # Buy
        ]
        dp[0][n - 1] = prices[n - 1] - fee
        for i in range(n - 2, -1, -1):
            dp[0][i] = max(dp[0][i + 1], dp[1][i + 1] + prices[i] - fee)
            dp[1][i] = max(dp[1][i + 1], dp[0][i + 1] - prices[i])
        return dp[1][0]

    # self.max_profit_top_down(prices, 0, fee, True, {})
    def max_profit_top_down(self, prices: list[int], idx: int, fee: int, can_buy: bool, memo: dict) -> int:
        n = len(prices)
        if idx >= n:
            return 0
        elif can_buy and idx >= n - 1:
            return 0
        elif (can_buy, idx) in memo:
            return memo[(can_buy, idx)]
        elif can_buy:
            memo[(True, idx)] = max(self.max_profit_top_down(prices, idx + 1, fee, True, memo),
                                    self.max_profit_top_down(prices, idx + 1, fee, False, memo) - prices[idx])
            return memo[(True, idx)]
        else:
            memo[(False, idx)] = max(self.max_profit_top_down(prices, idx + 1, fee, False, memo),
                                     self.max_profit_top_down(prices, idx + 1, fee, True, memo) + prices[idx] - fee)
            return memo[(False, idx)]


s = Solution()
print(s.maxProfit([1, 3, 2, 8, 4, 9], 2))
print(s.maxProfit([1, 3, 7, 5, 10, 3], 3))
print(s.maxProfit([7, 1, 5, 3, 6, 4], 1))
print(s.maxProfit([1, 2, 3, 4, 5], 2))
print(s.maxProfit([7, 6, 4, 3, 1], 3))
print(s.maxProfit(
    [48, 12, 60, 93, 97, 42, 25, 64, 17, 56, 85, 93, 9, 48, 52, 42, 58, 85, 81, 84, 69, 36, 1, 54, 23, 15, 72, 15, 11,
     94], 4))
