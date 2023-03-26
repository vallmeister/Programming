class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        return self.find_longest_chain_dp(pairs)

    def find_longest_chain_dp(self, pairs):
        pairs.sort(key=lambda x: x[0])
        n = len(pairs)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return dp[n - 1]


s = Solution()
print(s.find_longest_chain_dp([[1, 2], [2, 3], [3, 4]]))
print(s.find_longest_chain_dp([[1, 2], [7, 8], [4, 5]]))
print(s.find_longest_chain_dp([[7, 9], [4, 5], [7, 9], [-7, -1], [0, 10], [3, 10], [3, 6], [2, 3]]))
