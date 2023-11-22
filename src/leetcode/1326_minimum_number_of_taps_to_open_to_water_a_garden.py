import math
from functools import cache
from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        taps = []
        for idx, rng in enumerate(ranges):
            if rng == 0:
                continue
            start = max(0, idx - rng)
            end = min(n, idx + rng)
            taps.append((start, -end))
        taps.sort()
        if not taps:
            return -1
        curr_tap = taps[0]
        useful_taps = set()
        for tap in taps[1:]:
            start1, end1 = curr_tap
            start2, end2 = tap
            end1, end2 = -end1, -end2
            if end1 < end2:
                curr_tap = tap
            useful_taps.add((start1, -end1))
        if curr_tap == taps[-1]:
            useful_taps.add((curr_tap[0], curr_tap[1]))
        taps = list(useful_taps)
        taps.sort()
        del useful_taps

        @cache
        def recursive(i, curr_end):
            if curr_end == n:
                return 0
            elif i >= len(taps):
                return math.inf
            start, end = taps[i]
            if curr_end < start:
                return math.inf
            end = -end
            return min(1 + recursive(i + 1, end), recursive(i + 1, curr_end))

        ans = recursive(0, 0)
        if ans > n + 1:
            return -1
        return ans

    def min_taps_greedy(self, n, ranges):
        max_reach = [0] * (n + 1)
        for i in range(len(ranges)):
            start = max(0, i - ranges[i])
            end = min(n, i + ranges[i])

            max_reach[start] = max(max_reach[start], end)

        taps = 0
        curr_end = 0
        next_end = 0

        for i in range(n + 1):
            if i > next_end:
                return -1

            if i > curr_end:
                taps += 1
                curr_end = next_end

            next_end = max(next_end, max_reach[i])
        return taps


s = Solution()
print(s.minTaps(5, ranges=[3, 4, 1, 1, 0, 0]))
print(s.minTaps(3, ranges=[0, 0, 0, 0]))
print(s.minTaps(6, [1, 3, 2, 1, 1, 1]))
print(s.min_taps_greedy(5, ranges=[3, 4, 1, 1, 0, 0]))
print(s.min_taps_greedy(3, ranges=[0, 0, 0, 0]))
print(s.min_taps_greedy(6, [1, 3, 2, 1, 1, 1]))
