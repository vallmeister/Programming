class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        buy_after_sell = 0  # dp[1][i + 2]
        buy = 0  # dp[1][i + 1]
        sell = prices[n - 1]  # dp[0][i + 1]
        curr_buy = 0

        for i in range(n - 2, -1, -1):
            curr_sell = max(sell, buy_after_sell + prices[i])
            curr_buy = max(buy, sell - prices[i])
            buy_after_sell = buy
            buy = curr_buy
            sell = curr_sell

        return curr_buy

    def max_profit_dp(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[0] * (n + 1),  # sell
              [0] * (n + 1)]  # buy
        dp[0][n - 1] = prices[n - 1]
        for i in range(n - 2, -1, -1):
            dp[0][i] = max(dp[0][i + 1], dp[1][i + 2] + prices[i])
            dp[1][i] = max(dp[1][i + 1], dp[0][i + 1] - prices[i])
        return dp[1][0]

    # return self.max_profit_memo(prices, 0, True)
    def max_profit_memo(self, prices: list[int], idx: int, can_buy: bool, memo: dict) -> int:
        n = len(prices)
        if idx >= n:
            return 0
        elif can_buy and idx >= n - 1:
            return 0
        elif (can_buy, idx) in memo:
            return memo[(can_buy, idx)]
        elif can_buy:
            memo[(True, idx)] = max(self.max_profit_memo(prices, idx + 1, True, memo),
                                    self.max_profit_memo(prices, idx + 1, False, memo)
                                    - prices[idx])
            return memo[(True, idx)]
        else:
            memo[(False, idx)] = max(self.max_profit_memo(prices, idx + 1, False, memo),
                                     self.max_profit_memo(prices, idx + 2, True, memo)
                                     + prices[idx])
            return memo[(False, idx)]


s = Solution()
print(s.maxProfit([1, 2, 3, 0, 2]))
print(s.maxProfit([1]))
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([1, 2, 3, 4, 5]))
print(s.maxProfit([7, 6, 4, 3, 1]))
print(s.maxProfit(
    [48, 12, 60, 93, 97, 42, 25, 64, 17, 56, 85, 93, 9, 48, 52, 42, 58, 85, 81, 84, 69, 36, 1, 54, 23, 15, 72, 15, 11,
     94]))

print(s.max_profit_memo([1, 2, 3, 0, 2], 0, True, {}))
print(s.max_profit_memo([1], 0, True, {}))
print(s.max_profit_memo([7, 1, 5, 3, 6, 4], 0, True, {}))
print(s.max_profit_memo(
    [48, 12, 60, 93, 97, 42, 25, 64, 17, 56, 85, 93, 9, 48, 52, 42, 58, 85, 81, 84, 69, 36, 1, 54, 23, 15, 72, 15, 11,
     94], 0, True, {}))
