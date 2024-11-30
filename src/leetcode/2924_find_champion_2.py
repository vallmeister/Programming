from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        remaining = set(range(n))
        for _, v in edges:
            remaining.discard(v)
        if len(remaining) == 1:
            return remaining.pop()
        return -1


s = Solution()
print(s.findChampion(4, [[1, 3], [3, 0], [2, 0]]))
