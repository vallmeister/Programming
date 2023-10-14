from collections import Counter
from heapq import heappush, heappop
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for num, cnt in count.items():
            heappush(heap, (-cnt, num))
        ans = []
        for i in range(k):
            _, num = heappop(heap)
            ans.append(num)
        return ans


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], k=2))
print(s.topKFrequent([1], k=1))
