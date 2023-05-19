class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True


s = Solution()
print(s.canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
print(s.canAttendMeetings([[7, 10], [2, 4]]))
