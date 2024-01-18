from heapq import heappush, heappop
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        i = 0
        j = 0
        heap = [(nums1[i] + nums2[j], i, j)]
        visited = {(0, 0)}
        while k > 0 and heap:
            _, i, j = heappop(heap)
            ans.append([nums1[i], nums2[j]])
            k -= 1
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
        return ans


s = Solution()
print(s.kSmallestPairs([1, 7, 11], nums2=[2, 4, 6], k=3))
print(s.kSmallestPairs([1, 1, 2], nums2=[1, 2, 3], k=2))
print(s.kSmallestPairs([1, 2], nums2=[3], k=3))
