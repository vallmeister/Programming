class Solution:
    def minCostII(self, costs: list[list[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        for i in range(1, n):
            for j in range(k):
                prev_costs = []
                for m in range(k):
                    if j == m:
                        continue
                    prev_costs.append(costs[i - 1][m])
                costs[i][j] += min(prev_costs)
        return min(costs[n - 1])


s = Solution()
print(s.minCostII([[1, 5, 3], [2, 9, 4]]))
print(s.minCostII([[1, 3], [2, 4]]))
