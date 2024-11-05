class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        m = len(goal)
        n = len(s)
        if m != n:
            return False
        s *= 2
        n *= 2
        lps = self.lps(goal)
        i = j = 0
        while n - i > m - j:
            if goal[j] == s[i]:
                i += 1
                j += 1
            if j == m:
                return True
            elif i < n and goal[j] != s[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return False

    def lps(self, p):
        m = len(p)
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if p[i] == p[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps


sol = Solution()
print(sol.rotateString("abcde", "cdeab"))
