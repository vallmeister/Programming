from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [False] * n
        dp[0] = True
        indices = {stones[i]: i for i in range(n)}
        jumps = {i: set() for i in range(1, n)}
        if stones[1] != 1:
            return False
        dp[1] = True
        jumps[1].add(1)
        for i in range(1, n):
            if not dp[i]:
                continue
            for jump in jumps[i]:
                for k in range(max(1, jump - 1), jump + 2):
                    if stones[i] + k in indices:
                        idx = indices[stones[i] + k]
                        dp[idx] = True
                        jumps[idx].add(k)
        return dp[-1]


s = Solution()
print(s.canCross([0, 1, 3, 5, 6, 8, 12, 17]))
print(s.canCross([0, 1, 2, 3, 4, 8, 9, 11]))
