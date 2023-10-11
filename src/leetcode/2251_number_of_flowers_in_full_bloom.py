from heapq import heappush, heappop
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort()
        full_bloom_at = {}
        heap = []
        i = 0
        for person in sorted(people):
            while i < len(flowers) and flowers[i][0] <= person:
                heappush(heap, flowers[i][1])
                i += 1
            while heap and heap[0] < person:
                heappop(heap)
            full_bloom_at[person] = len(heap)
        return [full_bloom_at[t] for t in people]



s = Solution()
print(s.fullBloomFlowers([[1, 6], [3, 7], [9, 12], [4, 13]], people=[2, 3, 7, 11]))
print(s.fullBloomFlowers([[1, 10], [3, 3]], people=[3, 3, 2]))
print(s.fullBloomFlowers([[2, 6], [3, 7], [9, 12], [4, 13]], people=[1, 3, 7, 11]))
print(s.fullBloomFlowers([[19, 37], [19, 38], [19, 35]], [6, 7, 21, 1, 13, 37, 5, 37, 46, 43]))
print(s.fullBloomFlowers([[50, 50], [19, 27], [40, 46], [42, 48], [22, 46], [41, 50], [11, 36], [14, 29]],
                         [17, 35, 38]))  # 2, 2, 1
