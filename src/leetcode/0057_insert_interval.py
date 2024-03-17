from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        start, end = intervals[0]
        ans = []
        for s, e in intervals[1:]:
            if end < s:
                ans.append([start, end])
                start, end = s, e
            else:
                end = max(end, e)
        ans.append([start, end])
        return ans


sol = Solution()
print(sol.insert([[1, 3], [6, 9]], [2, 5]))
print(sol.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
