from collections import defaultdict
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        neighbors = defaultdict(set)
        for u, v in adjacentPairs:
            neighbors[u].add(v)
            neighbors[v].add(u)
        starting_nums = {num for num in neighbors if len(neighbors[num]) == 1}
        ans = []
        visited = set()
        for num in starting_nums:
            while num not in visited:
                visited.add(num)
                ans.append(num)
                for nxt in neighbors[num]:
                    if nxt in visited:
                        continue
                    num = nxt
        return ans


s = Solution()
print(s.restoreArray([[2, 1], [3, 4], [3, 2]]))
print(s.restoreArray([[4, -2], [1, 4], [-3, 1]]))
print(s.restoreArray([[100000, -100000]]))
