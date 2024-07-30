import math


class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        bs_before = [0] * n
        as_after = [0] * n
        for i in range(1, n):
            bs_before[i] = bs_before[i - 1] + (1 if s[i - 1] == 'b' else 0)
        for i in reversed(range(n - 1)):
            as_after[i] = as_after[i + 1] + (1 if s[i + 1] == 'a' else 0)
        min_so_far = math.inf
        for i in range(n):
            min_so_far = min(min_so_far, bs_before[i] + as_after[i])
        return min_so_far


sol = Solution()
print(sol.minimumDeletions("aababbab"))
