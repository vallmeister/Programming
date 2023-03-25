class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        return self.minimum_delete_sum_dp(s1, s2)

    def minimum_delete_sum_dp(self, s1, s2):
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i >= m and j >= n:
                    dp[i][j] = 0
                elif i >= m:
                    dp[i][j] = ord(s2[j]) + dp[i][j + 1]
                elif j >= n:
                    dp[i][j] = ord(s1[i]) + dp[i + 1][j]
                elif s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(ord(s1[i]) + dp[i + 1][j], ord(s2[j]) + dp[i][j + 1])
        return dp[0][0]

    def minimum_delete_sum_memo(self, s1, s2):
        memo = {}

        def minimum_delete_sum(i, j):
            if i >= len(s1) and j >= len(s2):
                return 0
            elif (i, j) in memo:
                return memo[(i, j)]
            elif i >= len(s1):
                memo[(i, j)] = ord(s2[j]) + minimum_delete_sum(i, j + 1)
                return memo[(i, j)]
            elif j >= len(s2):
                memo[(i, j)] = ord(s1[i]) + minimum_delete_sum(i + 1, j)
                return memo[(i, j)]
            elif s1[i] == s2[j]:
                memo[(i, j)] = minimum_delete_sum(i + 1, j + 1)
                return memo[(i, j)]
            else:  # Since deleting a character in s1 or adding it to s2 is equivalent, we prefer to always delete
                memo[(i, j)] = min(ord(s1[i]) + minimum_delete_sum(i + 1, j), ord(s2[j]) + minimum_delete_sum(i, j + 1))
                return memo[(i, j)]

        return minimum_delete_sum(0, 0)


s = Solution()
print(s.minimumDeleteSum('sea', 'eat'))
print(s.minimumDeleteSum('delete', 'leet'))
