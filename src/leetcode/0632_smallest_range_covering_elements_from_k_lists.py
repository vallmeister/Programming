import math
from heapq import heappush, heappop
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_elements = []
        curr_max = -math.inf
        for i, ls in enumerate(nums):
            fst = ls[0]
            curr_max = max(curr_max, fst)
            heappush(min_elements, (fst, i, 0))
        ans = [min_elements[0][0], curr_max]
        while min_elements[0][2] + 1 < len(nums[min_elements[0][1]]):
            _, list_i, num_j = heappop(min_elements)
            num_j += 1
            element = nums[list_i][num_j]
            heappush(min_elements, (element, list_i, num_j))
            curr_max = max(curr_max, element)
            curr_min = min_elements[0][0]
            a, b = ans
            if curr_max - curr_min < b - a:
                ans = [curr_min, curr_max]
        return ans


s = Solution()
print(s.smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
