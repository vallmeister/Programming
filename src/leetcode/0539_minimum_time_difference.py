from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for tp in timePoints:
            hh, mm = tp.split(":")
            times.append(60 * int(hh) + int(mm))
        times.sort()
        ans = 1440
        for i in range(len(times)):
            prev = times[i - 1]
            time = times[i]
            ans = min(ans, abs(time - prev), abs(time + 1440 - prev))
        return ans


s = Solution()
print(s.findMinDifference(["23:59", "00:00"]))
print(s.findMinDifference(["00:00", "23:59", "00:00"]))
