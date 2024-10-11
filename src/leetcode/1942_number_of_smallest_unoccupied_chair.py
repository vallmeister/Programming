from heapq import heappop, heappush
from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        sorted_times = list(sorted(enumerate(times), key=lambda x: x[1]))
        next_chair = 0
        curr_guests = []
        empty_chairs = []
        for friend, (arrival, leaving) in sorted_times:
            while curr_guests and curr_guests[0][0] <= arrival:
                _, free_chair = heappop(curr_guests)
                heappush(empty_chairs, free_chair)
            chair = next_chair
            if empty_chairs:
                chair = heappop(empty_chairs)
            else:
                next_chair += 1
            if friend == targetFriend:
                return chair
            heappush(curr_guests, (leaving, chair))
        return -1


s = Solution()
print(s.smallestChair([[1, 4], [2, 3], [4, 6]], 1))
