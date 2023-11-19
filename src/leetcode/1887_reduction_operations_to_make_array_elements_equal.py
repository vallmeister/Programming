from collections import Counter
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        heap = [(-num, cnt) for num, cnt in Counter(nums).items()]
        heapify(heap)
        ans = 0
        while len(heap) > 1:
            _, cnt = heappop(heap)
            next_largest, next_cnt = heappop(heap)
            next_largest = -next_largest
            ans += cnt
            heappush(heap, (-next_largest, cnt + next_cnt))
        return ans


s = Solution()
print(s.reductionOperations([5, 1, 3]))
print(s.reductionOperations([1, 1, 1]))
print(s.reductionOperations([1, 1, 2, 2, 3]))
