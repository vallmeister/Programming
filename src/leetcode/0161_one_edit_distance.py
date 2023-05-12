class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) == 0:
            for i in range(len(s)):
                if s[i] != t[i]:
                    return s[i + 1:] == t[i + 1:]
        elif abs(len(s) - len(t)) == 1:
            if len(s) > len(t):
                s, t = t, s

            for i in range(len(s)):
                if s[i] != t[i]:
                    return s[i:] == t[i + 1:]
        return len(s) + 1 == len(t)


sol = Solution()
print(sol.isOneEditDistance('ab', 'acb'))
print(sol.isOneEditDistance('', ''))
print(sol.isOneEditDistance('a', ''))
print(sol.isOneEditDistance('a', 'ac'))
