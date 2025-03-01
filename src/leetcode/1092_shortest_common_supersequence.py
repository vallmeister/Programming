class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in reversed(range(m + 1)):
            for j in reversed(range(n + 1)):
                if i == m and j == n:
                    continue
                elif i == m:
                    dp[i][j] = 1 + dp[i][j + 1]
                elif j == n:
                    dp[i][j] = 1 + dp[i + 1][j]
                elif str1[i] == str2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1])

        ans = []
        i = j = 0
        for _ in range(dp[0][0]):
            if i == m:
                ans.append(str2[j])
                j += 1
            elif j == n:
                ans.append(str1[i])
                i += 1
            elif str1[i] == str2[j]:
                ans.append(str1[i])
                i += 1
                j += 1
            elif dp[i + 1][j] < dp[i][j + 1]:
                ans.append(str1[i])
                i += 1
            else:
                ans.append(str2[j])
                j += 1
        return ''.join(ans)


s = Solution()
print(s.shortestCommonSupersequence(str1="abac", str2="cab"))
print(s.shortestCommonSupersequence(str1="aaaaaaaa", str2="aaaaaaaa"))
