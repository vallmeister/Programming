class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        last = prices[0]
        for p in prices[1:]:
            diff = p - last
            if diff > 0:
                profit += diff
            last = p
        return profit


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([1, 2, 3, 4, 5]))
print(s.maxProfit([7, 6, 4, 3, 1]))
