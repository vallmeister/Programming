from heapq import heappush, heappop


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        available = [0]
        rooms = 1
        for start, end in intervals:
            if start < available[0]:
                rooms += 1
                heappush(available, end)
            else:
                heappop(available)
                heappush(available, end)

        return rooms


s = Solution()
print(s.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
print(s.minMeetingRooms([[7, 10], [2, 4]]))
