class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        prev = prices[0]
        for p in prices[1:]:
            diff = p - prev
            if diff > 0:
                profit += diff
            prev = p
        return profit


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([1, 2, 3, 4, 5]))
print(s.maxProfit([7, 6, 4, 3, 1]))
