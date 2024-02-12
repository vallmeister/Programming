from collections import defaultdict


class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ans = 0
        m, n = len(s), len(t)
        equal_prev = [0] * (n + 1)
        unequal_prev = [0] * (n + 1)
        for i in range(m):
            equal_curr = [0] * (n + 1)
            unequal_curr = [0] * (n + 1)
            for j in range(n):
                if s[i] == t[j]:
                    equal_curr[j + 1] = 1 + equal_prev[j]
                    unequal_curr[j + 1] = unequal_prev[j]
                else:
                    unequal_curr[j + 1] = 1 + equal_prev[j]
                ans += unequal_curr[j + 1]
            equal_prev, unequal_prev = equal_curr, unequal_curr
        return ans
