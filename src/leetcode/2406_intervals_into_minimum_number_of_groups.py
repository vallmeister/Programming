from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        n = max(max(interval) for interval in intervals)
        start = [0] * (n + 1)
        end = [0] * (n + 1)
        for left, right in intervals:
            start[left] += 1
            end[right] += 1
        ans = ps = 0
        for i in range(n + 1):
            ps += start[i]
            ans = max(ans, ps)
            ps -= end[i]
        return ans


s = Solution()
print(s.minGroups([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]))
