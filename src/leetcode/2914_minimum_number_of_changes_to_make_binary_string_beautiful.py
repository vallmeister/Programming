class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0
        for i in range(0, len(s), 2):
            ans += abs(int(s[i]) - int(s[i + 1]))
        return ans
