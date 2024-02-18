from heapq import heappop, heappush
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        free_rooms = [i for i in range(n)]
        used_rooms = []
        count = [0] * n
        meetings.sort(reverse=True)
        time = 0
        while meetings:
            while used_rooms and used_rooms[0][0] <= time:
                _, room = heappop(used_rooms)
                heappush(free_rooms, room)
            while free_rooms and meetings and meetings[-1][0] <= time:
                start, end = meetings.pop()
                room = heappop(free_rooms)
                count[room] += 1
                heappush(used_rooms, (time + end - start, room))
            if not free_rooms:
                time = used_rooms[0][0]
            else:
                time += 1
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i
        return -1


s = Solution()
print(s.mostBooked(2, meetings=[[0, 10], [1, 5], [2, 7], [3, 4]]))
print(s.mostBooked(3, meetings=[[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]))
print(s.mostBooked(3, [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6]]))
