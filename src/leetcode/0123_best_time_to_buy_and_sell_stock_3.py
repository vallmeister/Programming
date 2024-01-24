from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        prefix_profit = [0] * n
        suffix_profit = [0] * n
        min_so_far = prices[0]
        for i in range(1, n):
            prefix_profit[i] = max(prefix_profit[i - 1], prices[i] - min_so_far)
            min_so_far = min(min_so_far, prices[i])
        max_so_far = prices[-1]
        for i in reversed(range(n - 1)):
            suffix_profit[i] = max(suffix_profit[i + 1], max_so_far - prices[i])
            max_so_far = max(max_so_far, prices[i])
        ans = 0
        for i in range(n):
            ans = max(ans, prefix_profit[i] + suffix_profit[i])
        return ans


s = Solution()
print(s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
print(s.maxProfit([1, 2, 3, 4, 5]))
print(s.maxProfit([7, 6, 4, 3, 1]))
