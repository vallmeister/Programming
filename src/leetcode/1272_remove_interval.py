class Solution:
    def removeInterval(self, intervals: list[list[int]], toBeRemoved: list[int]) -> list[list[int]]:
        new_intervals = []
        for start, end in intervals:
            if toBeRemoved[0] <= start and end <= toBeRemoved[1]:
                continue
            elif start < toBeRemoved[0] and toBeRemoved[1] < end:
                new_intervals.append([start, toBeRemoved[0]])
                new_intervals.append([toBeRemoved[1], end])
            elif toBeRemoved[0] <= start <= toBeRemoved[1] < end:
                new_intervals.append([toBeRemoved[1], end])
            elif start < toBeRemoved[0] <= end <= toBeRemoved[1]:
                new_intervals.append([start, toBeRemoved[0]])
            else:
                new_intervals.append([start, end])
        return new_intervals


s = Solution()
print(s.removeInterval([[0, 2], [3, 4], [5, 7]], toBeRemoved=[1, 6]))
print(s.removeInterval([[0, 5]], toBeRemoved=[2, 3]))
print(s.removeInterval([[-5, -4], [-3, -2], [1, 2], [3, 5], [8, 9]], toBeRemoved=[-1, 4]))
print(s.removeInterval([[0, 100]], [0, 50]))
