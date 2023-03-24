class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        n = len(costs)
        dp = costs[0]
        for i in range(1, n):
            new_dp = [0] * 3
            new_dp[0] = costs[i][0] + min(dp[1], dp[2])
            new_dp[1] = costs[i][1] + min(dp[0], dp[2])
            new_dp[2] = costs[i][2] + min(dp[0], dp[1])
            dp = new_dp
        return min(dp)

    def min_cost_dp(self, costs):
        n = len(costs)
        dp = [[0] * 3 for _ in range(n)]
        dp[0] = costs[0]
        for i in range(1, n):
            dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])
        return min(dp[n - 1])

    def min_cost_memo(self, costs):
        memo = {}
        n = len(costs)

        def min_cost(i, color):
            if (i, color) in memo:
                return memo[(i, color)]
            elif i >= n:
                return 0
            else:
                memo[(i, color)] = costs[i][color]
                if color == 0:
                    memo[(i, color)] += min(min_cost(i + 1, 1), min_cost(i + 1, 2))
                elif color == 1:
                    memo[(i, color)] += + min(min_cost(i + 1, 0), min_cost(i + 1, 2))
                elif color == 2:
                    memo[(i, color)] += min(min_cost(i + 1, 0), min_cost(i + 1, 1))
                return memo[(i, color)]

        return min(min_cost(0, 0), min_cost(0, 1), min_cost(0, 2))


s = Solution()
print(s.minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]))
print(s.minCost([[7, 6, 2]]))
