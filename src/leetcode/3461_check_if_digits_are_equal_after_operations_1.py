class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = [int(c) for c in s]
        while len(s) > 2:
            ss = []
            n = len(s)
            for i in range(1, n):
                ss.append((s[i - 1] + s[i]) % 10)
            s = ss
        return s[0] == s[1]


sol = Solution()
print(sol.hasSameDigits('3902'))
