from heapq import heappush, heappop
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        heap = []
        for i in range(len(nums)):
            row = nums[i]
            index = i * (i + 1) // 2
            step = i + 2
            for j in range(len(row)):
                heappush(heap, (index, nums[i][j]))
                index += step
                step += 1
        while heap:
            _, element = heappop(heap)
            ans.append(element)
        return ans


s = Solution()
print(s.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.findDiagonalOrder([[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]))
