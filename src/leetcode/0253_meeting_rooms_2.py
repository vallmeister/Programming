import heapq

class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        rooms = 1
        heap = [intervals[0][1]]
        for i in range(1, len(intervals)):
            next_available = heapq.heappop(heap)
            if intervals[i][0] < next_available:
                heapq.heappush(heap, next_available)
                rooms += 1
            heapq.heappush(heap, intervals[i][1])

        return rooms


s = Solution()
print(s.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
print(s.minMeetingRooms([[7, 10], [2, 4]]))
