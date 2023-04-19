class Solution:
    def arrangeCoins(self, n: int) -> int:
        # To obtain m stairs, we need the sum from 1 to m which is m * (m + 1) / 2
        left = 1
        right = n
        while left <= right:
            m = (left + right) // 2
            if m * (m + 1) <= 2 * n < (m + 1) * (m + 2):
                return m
            elif m * (m + 1) < 2 * n:
                left = m + 1
            elif m * (m + 1) > 2 * n:
                right = m - 1
        return left


s = Solution()
print(s.arrangeCoins(5))
print(s.arrangeCoins(8))
print(s.arrangeCoins(45))
print(s.arrangeCoins(46))
