class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        offset = ord('a')
        ans = 0
        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - offset] += 1
                if self.is_balanced(freq):
                    ans = max(ans, j - i + 1)
        return ans

    def is_balanced(self, freq):
        occurrence = max(freq)
        return all(f == 0 or f == occurrence for f in freq)


s = Solution()
print(s.longestBalanced("abbac"))
print(s.longestBalanced("zzabccy"))
print(s.longestBalanced("aba"))
