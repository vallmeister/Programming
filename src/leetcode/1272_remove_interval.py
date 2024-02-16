class Solution:
    def removeInterval(self, intervals: list[list[int]], toBeRemoved: list[int]) -> list[list[int]]:
        new_intervals = []
        left, right = toBeRemoved
        for start, end in intervals:
            if left <= start and end <= right:
                continue
            elif start < left <= end <= right:
                new_intervals.append([start, left])
            elif left <= start < right <= end:
                new_intervals.append([right, end])
            elif start < left and right < end:
                new_intervals.append([start, left])
                new_intervals.append([right, end])
            else:
                new_intervals.append([start, end])
        return new_intervals


s = Solution()
print(s.removeInterval([[0, 2], [3, 4], [5, 7]], toBeRemoved=[1, 6]))
print(s.removeInterval([[0, 5]], toBeRemoved=[2, 3]))
print(s.removeInterval([[-5, -4], [-3, -2], [1, 2], [3, 5], [8, 9]], toBeRemoved=[-1, 4]))
print(s.removeInterval([[0, 100]], [0, 50]))
