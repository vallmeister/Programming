from collections import deque
from heapq import heappush, heappop
from typing import List


class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        nums = deque(nums)
        ps = ans = 0
        heap = []
        while nums:
            num = nums.popleft()
            ps += num
            if num < 0:
                heappush(heap, num)
            if ps < 0:
                smallest = heappop(heap)
                ps -= smallest
                nums.append(smallest)
                ans += 1
        return ans


s = Solution()
print(s.makePrefSumNonNegative([-3, -1, 1, 0, 3, 0, 5, 5, -1, 1, -4, 4, 4, -2]))
print(s.makePrefSumNonNegative([6, -6, -3, 3, 1, 5, -4, -3, -2, -3, 4, -1, 4, 4, -2, 6, 0]))
