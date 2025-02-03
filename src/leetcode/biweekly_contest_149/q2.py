from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        k += 1
        n = len(startTime)
        events = sorted(zip(startTime, endTime))
        free_times = []
        prev_end = 0
        for i in range(n):
            start, end = events[i]
            free_times.append(start - prev_end)
            prev_end = end
        free_times.append(eventTime - prev_end)

        window = sum(free_times[:k - 1])
        ans = window
        left = 0
        for right in range(k - 1, len(free_times)):
            window += free_times[right]
            ans = max(ans, window)
            window -= free_times[left]
            left += 1
        return ans


s = Solution()
print(s.maxFreeTime(eventTime=5, k=1, startTime=[1, 3], endTime=[2, 5]))
print(s.maxFreeTime(eventTime=10, k=1, startTime=[0, 2, 9], endTime=[1, 4, 10]))
print(s.maxFreeTime(eventTime=5, k=2, startTime=[0, 1, 2, 3, 4], endTime=[1, 2, 3, 4, 5]))
print(s.maxFreeTime(34, 2, [0, 17], [14, 19]))
