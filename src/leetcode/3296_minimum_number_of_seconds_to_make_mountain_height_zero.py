import bisect
import math
from typing import List


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        geometric_sum = []
        for i in range(10 ** 5 + 1):
            geometric_sum.append(i * (i + 1) // 2)
        left = 1
        right = math.ceil(mountainHeight / len(workerTimes))
        right = geometric_sum[right] * max(workerTimes)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            height = self.height_after_n_sec(mid, workerTimes, geometric_sum)
            if height >= mountainHeight:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def height_after_n_sec(self, n, worker_times, geometric_sum):
        height = 0
        for time in worker_times:
            x = n // time
            ip = bisect.bisect_left(geometric_sum, x)
            if geometric_sum[ip] > x:
                ip -= 1
            height += ip
        return height


s = Solution()
print(s.minNumberOfSeconds(4, [2, 1, 1]))
print(s.minNumberOfSeconds(100000, [1]))
