import math


class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[list[int]]) -> int:
        m = len(requests)
        states = 2 ** m
        dp = [[math.inf] * m for _ in range(states)]
        for mask in range(states):
            for i in range(m):
                if mask == 0:
                    dp[mask][i] = 0
                    continue
                elif mask & (1 << i) == 0:
                    continue
                prev_mask = mask ^ (1 << i)
                arrival, floor = requests[i]
                if prev_mask == 0:
                    dp[mask][i] = max(arrival, abs(floor - start))
                    continue
                for j in range(m):
                    _, prev_floor = requests[j]
                    dp[mask][i] = min(dp[mask][i], max(arrival, dp[prev_mask][j] + abs(floor - prev_floor)))

        return min(dp[states - 1])


s = Solution()
print(s.elevatorRequests(n=9, start=0, requests=[[0, 8], [6, 5]]))
print(s.elevatorRequests(n=8, start=5, requests=[[1, 7], [7, 3]]))
print(s.elevatorRequests(n=7, start=3, requests=[[0, 5], [0, 1], [6, 3]]))
