from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        events = sorted(zip(startTime, endTime))
        free_times = []
        prev_end = 0
        for i in range(n):
            start, end = events[i]
            free_times.append(start - prev_end)
            prev_end = end
        free_times.append(eventTime - prev_end)

        max_free_block_before = [0] * n
        max_free_block_before[0] = free_times[0]
        for i in range(1, n):
            max_free_block_before[i] = max(max_free_block_before[i - 1], free_times[i])

        max_free_block_after = [0] * n
        max_free_block_after[-1] = free_times[-1]
        for i in reversed(range(n - 1)):
            max_free_block_after[i] = max(max_free_block_after[i + 1], free_times[i + 1])

        ans = max(free_times)
        for i in range(n):
            start, end = events[i]
            duration = end - start
            ans = max(ans, free_times[i] + free_times[i + 1])

            ip = self.bin_search_left(max_free_block_before, duration)
            if ip < i:
                ans = max(ans, free_times[i] + free_times[i + 1] + duration)

            ip = self.bin_search_right(max_free_block_after, duration)
            if ip > i:
                ans = max(ans, free_times[i] + free_times[i + 1] + duration)

        return ans

    def bin_search_left(self, arr, target):
        n = len(arr)
        left = 0
        right = n - 1
        ip = n
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= target:
                ip = min(ip, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ip

    def bin_search_right(self, arr, target):
        n = len(arr)
        left = 0
        right = n - 1
        ip = 0
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= target:
                ip = max(ip, mid)
                left = mid + 1
            else:
                right = mid - 1
        return ip


s = Solution()
print(s.maxFreeTime(eventTime=5, startTime=[1, 3], endTime=[2, 5]))
print(s.maxFreeTime(eventTime=10, startTime=[0, 7, 9], endTime=[1, 8, 10]))
print(s.maxFreeTime(eventTime=10, startTime=[0, 3, 7, 9], endTime=[1, 4, 8, 10]))
print(s.maxFreeTime(eventTime=5, startTime=[0, 1, 2, 3, 4], endTime=[1, 2, 3, 4, 5]))
print(s.maxFreeTime(99, [3, 16, 97], [12, 66, 98]))
