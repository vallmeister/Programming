from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        m = 301
        dp = {}
        ans = 0
        for i, num in enumerate(nums):
            best = 1
            for diff in reversed(range(m)):
                if num + diff < m and (num + diff, diff) in dp:
                    best = max(best, 1 + dp[(num + diff, diff)])
                if num - diff >= 0 and (num - diff, diff) in dp:
                    best = max(best, 1 + dp[(num - diff, diff)])
                dp[(num, diff)] = best
                ans = max(ans, best)
        return ans


s = Solution()
print(s.longestSubsequence([16, 6, 3]))
print(s.longestSubsequence([6, 5, 3, 4, 2, 1]))
print(s.longestSubsequence([10, 20, 10, 19, 10, 20]))
print(s.longestSubsequence([1, 8]))
