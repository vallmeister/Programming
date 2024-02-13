from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in reversed(range(n)):
            for j in range(n):
                dp[i][j] = j <= i or s[i] == s[j] and dp[i + 1][j - 1]
        ans = []

        def backtracking(idx, curr_partition):
            if idx == n:
                ans.append(list(curr_partition))
                return
            for end in range(idx, n):
                if dp[idx][end]:
                    curr_partition.append(s[idx:end + 1])
                    backtracking(end + 1, curr_partition)
                    curr_partition.pop()

        backtracking(0, [])
        return ans


print(Solution().partition('aab'))
