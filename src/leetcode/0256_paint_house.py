class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        n = len(costs)
        dp = [[0] * 3 for _ in range(n)]
        dp[0] = costs[0]
        for house in range(1, n):
            for color in range(3):
                prev_cost = []
                for not_color in range(3):
                    if color == not_color:
                        continue
                    prev_cost.append(dp[house - 1][not_color])
                dp[house][color] = min(prev_cost) + costs[house][color]
        return min(dp[-1])


s = Solution()
print(s.minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]))
print(s.minCost([[7, 6, 2]]))
