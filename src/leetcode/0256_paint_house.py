class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        n = len(costs)
        prev_house = costs[0]
        for i in range(1, n):
            curr_house = costs[i]
            curr_house[0] += min(prev_house[1], prev_house[2])
            curr_house[1] += min(prev_house[0], prev_house[2])
            curr_house[2] += min(prev_house[0], prev_house[1])
            prev_house = curr_house
        return min(costs[-1])


s = Solution()
print(s.minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]))
print(s.minCost([[7, 6, 2]]))
