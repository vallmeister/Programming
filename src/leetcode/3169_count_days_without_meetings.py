from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        prev_end = 0
        ans = 0
        for start, end in meetings:
            if start > prev_end:
                ans += start - prev_end - 1
            prev_end = max(prev_end, end)
        ans += days - prev_end
        return ans
