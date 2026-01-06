class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(min(n, limit) + 1):
            candies = n - i
            if candies > 2 * limit:
                continue
            ans += min(candies, limit) + 1 - max(0, candies - limit)
        return ans


s = Solution()
print(s.distributeCandies(n=5, limit=2))
print(s.distributeCandies(3, 3))
