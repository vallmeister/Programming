from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        ans = 0
        n = len(events)
        events.sort()

        max_value = [0] * n
        max_value[-1] = events[-1][2]
        for i in reversed(range(n - 1)):
            max_value[i] = max(max_value[i + 1], events[i][2])

        for i in range(n):
            _, end, value = events[i]
            j = self.binary_search(events, end + 1)
            if j < n:
                value += max_value[j]
            ans = max(ans, value)
        return ans

    def binary_search(self, events, time):
        n = len(events)
        ip = n
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if events[mid][0] >= time:
                ip = mid
                right = mid - 1
            else:
                left = mid + 1
        return ip


s = Solution()
print(s.maxTwoEvents([[1, 3, 2], [4, 5, 2], [2, 4, 3]]))
print(s.maxTwoEvents([[1, 3, 2], [4, 5, 2], [1, 5, 5]]))
print(s.maxTwoEvents([[1, 5, 3], [1, 5, 1], [6, 6, 5]]))
