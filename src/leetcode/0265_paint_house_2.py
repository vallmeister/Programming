import math


class Solution:
    def minCostII(self, costs: list[list[int]]) -> int:
        n = len(costs)
        prev_house = costs[0]
        k = len(prev_house)
        for i in range(1, n):
            curr_house = costs[i]
            for color in range(k):
                prev_color = math.inf
                for j in range(k):
                    if color == j:
                        continue
                    prev_color = min(prev_color, prev_house[j])
                curr_house[color] += prev_color
            prev_house = curr_house
        return min(costs[-1])


s = Solution()
print(s.minCostII([[1, 5, 3], [2, 9, 4]]))
print(s.minCostII([[1, 3], [2, 4]]))
