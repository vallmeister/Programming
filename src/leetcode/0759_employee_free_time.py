from collections import defaultdict


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        ans = []
        line_sweep = defaultdict(int)
        for intervals in schedule:
            for interval in intervals:
                line_sweep[interval.start] += 1
                line_sweep[interval.end] -= 1
        keys = list(reversed(sorted(line_sweep.keys())))
        count = line_sweep[keys.pop()]
        while keys:
            while keys and count > 0:
                start = keys.pop()
                count += line_sweep[start]
            if keys and count == 0:
                end = keys.pop()
                ans.append(Interval(start, end))
                count = line_sweep[end]
        return ans


s = Solution()
print([(interval.start, interval.end) for interval in
       s.employeeFreeTime(schedule=[[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)], [Interval(4, 10)]])])
print([(interval.start, interval.end) for interval in
       s.employeeFreeTime(schedule=[[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]])])
