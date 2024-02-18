from heapq import heappush, heappop
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []
        ans = 0
        while ans < n - 1:
            diff = heights[ans + 1] - heights[ans]
            if diff > 0:
                heappush(heap, diff)
                if len(heap) > ladders:
                    bricks -= heappop(heap)
                if bricks < 0:
                    break
            ans += 1

        return ans


s = Solution()
print(s.furthestBuilding([4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1))
print(s.furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2))
print(s.furthestBuilding([14, 3, 19, 3], bricks=17, ladders=0))
