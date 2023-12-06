class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        ans = weeks * 28 + 7 * weeks * (weeks - 1) // 2
        days = n % 7
        ans += (weeks + days) * (weeks + days + 1) // 2 - weeks * (weeks + 1) // 2
        return ans


s = Solution()
print(s.totalMoney(4))
print(s.totalMoney(10))
print(s.totalMoney(20))
