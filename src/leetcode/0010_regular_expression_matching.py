class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        stars = [False] * (n + 1)
        for i in range(n):
            stars[i] = p[i] == '*'

        def recursive(i, j, state):
            if state == 0 and i == m and j == n:
                return True

        return recursive(0, 0, 0)


sol = Solution()
print(sol.isMatch("aa", p="a"))
print(sol.isMatch("aa", p="a*"))
print(sol.isMatch("ab", p=".*"))
print(sol.isMatch('abc', 'a.c'))
print(sol.isMatch('abc', 'a.*'))
print(sol.isMatch('abc', 'ab*'))
print('ab', '.*c')  # TODO: fix this with DP
