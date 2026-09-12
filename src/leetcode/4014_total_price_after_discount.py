class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        n = len(discounts)
        ans = j = 0
        for p in prices:
            if j < n:
                p = (p * (100 - discounts[j])) / 100
                p = round(p, 6)
                j += 1
            ans += p
        return ans


s = Solution()
print(s.minPrice(prices=[10, 30, 21], discounts=[50, 60]))
print(s.minPrice(prices=[100, 70], discounts=[10, 40, 50]))
print(s.minPrice(prices=[7, 3, 9], discounts=[100, 100]))
