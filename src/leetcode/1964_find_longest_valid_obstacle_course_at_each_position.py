from bisect import bisect_right
from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        dp = [1] * n
        lis = []
        for i in range(n):
            h = obstacles[i]
            ip = bisect_right(lis, h)
            if ip == len(lis):
                lis.append(h)
            else:
                lis[ip] = h
            dp[i] = ip + 1

        return dp
