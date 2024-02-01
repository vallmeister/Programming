from collections import deque
from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ms = []
        n = len(heights)
        for i in range(n):
            while ms and heights[ms[-1]] <= heights[i]:
                ms.pop()
            ms.append(i)
        return ms

    def find_buildings_optimized(self, heights):
        ans = deque()
        max_height = 0
        for i in reversed(range(len(heights))):
            if heights[i] > max_height:
                ans.appendleft(i)
                max_height = heights[i]
        return ans
