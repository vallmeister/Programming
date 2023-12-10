from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        start, end = intervals[0]
        for next_start, next_end in intervals[1:]:
            if next_start <= end:
                end = max(end, next_end)
            else:
                ans.append([start, end])
                start, end = next_start, next_end
        else:
            ans.append([start, end])
        return ans


s = Solution()
print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(s.merge([[1, 4], [4, 5]]))
