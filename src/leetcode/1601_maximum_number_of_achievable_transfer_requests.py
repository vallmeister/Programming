import math
from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        transfers = [0] * n
        m = len(requests)

        def backtracking(i):
            if i >= m:
                if all(transfers[i] == 0 for i in range(n)):
                    return 0
                else:
                    return -math.inf
            no_take = backtracking(i + 1)
            s, t = requests[i]
            transfers[s] -= 1
            transfers[t] += 1
            take = 1 + backtracking(i + 1)
            transfers[s] += 1
            transfers[t] -= 1
            return max(no_take, take)

        return backtracking(0)


sol = Solution()
print(sol.maximumRequests(n=5, requests=[[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]))
print(sol.maximumRequests(n=3, requests=[[0, 0], [1, 2], [2, 1]]))
