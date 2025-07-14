from collections import defaultdict
from heapq import heappush, heappop
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        start_to_event = defaultdict(list)
        event_ends = defaultdict(int)
        max_end = 0
        for i, (start, end) in enumerate(events):
            start_to_event[start].append(i)
            max_end = max(max_end, end)
            event_ends[i] = end
        candidates = []
        ans = 0
        for day in range(max_end + 1):
            # pop events that are already over
            while candidates and candidates[0][0] < day:
                heappop(candidates)

            # add events that start on current day
            for event in start_to_event[day]:
                heappush(candidates, (event_ends[event], event))

            # attend event today that ends earliest
            if candidates:
                heappop(candidates)
                ans += 1
        return ans

s = Solution()
print(s.maxEvents([[1, 2], [2, 3], [3, 4]]))
print(s.maxEvents([[1, 2], [2, 3], [3, 4], [1, 2]]))
