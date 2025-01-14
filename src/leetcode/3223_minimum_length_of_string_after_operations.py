from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)
        ans = 0
        for v in counter.values():
            ans += min(v, 2 - (v % 2))
        return ans


sol = Solution()
print(sol.minimumLength("abaacbcbb"))
