from bisect import bisect_left
from functools import cache
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()
        startTime = [start for start, _, _ in jobs]

        @cache
        def recursive(idx):
            if idx == len(jobs):
                return 0
            _, end, p = jobs[idx]
            next_idx = bisect_left(startTime, end)
            return max(recursive(idx + 1), p + recursive(next_idx))

        def dynamic_programming():
            n = len(jobs)
            dp = [0] * (n + 1)
            for i in reversed(range(n)):
                _, end, p = jobs[i]
                next_idx = bisect_left(startTime, end)
                dp[i] = max(dp[i + 1], p + dp[next_idx])

            return max(dp)

        return dynamic_programming()


s = Solution()
print(s.jobScheduling([1, 2, 3, 3], endTime=[3, 4, 5, 6], profit=[50, 10, 40, 70]))
print(s.jobScheduling([1, 2, 3, 4, 6], endTime=[3, 5, 10, 6, 9], profit=[20, 20, 100, 70, 60]))
print(s.jobScheduling([1, 1, 1], endTime=[2, 3, 4], profit=[5, 6, 4]))
