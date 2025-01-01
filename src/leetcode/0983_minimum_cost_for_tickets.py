from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 367
        for i in reversed(range(366)):
            if days and days[-1] == i:
                dp[i] = min(dp[i + 1] + costs[0], dp[min(i + 7, 365)] + costs[1], dp[min(i + 30, 365)] + costs[2])
                days.pop()
            else:
                dp[i] = dp[i + 1]
        return dp[0]


s = Solution()
print(s.mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))
