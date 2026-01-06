from functools import cache


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:

        @cache
        def memo(i, candies):
            if i >= 3:
                if candies == 0:
                    return 1
                else:
                    return 0
            ans = 0
            for j in range(min(limit, candies) + 1):
                ans += memo(i + 1, candies - j)
            return ans

        return memo(0, n)


s = Solution()
print(s.distributeCandies(n=5, limit=2))
print(s.distributeCandies(3, 3))
