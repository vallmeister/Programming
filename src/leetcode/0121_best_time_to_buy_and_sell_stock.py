class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min_so_far = prices[0]
        for p in prices[1:]:
            profit = max(p - min_so_far, profit)
            min_so_far = min(p, min_so_far)
        return profit


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([7, 6, 4, 3, 1]))
