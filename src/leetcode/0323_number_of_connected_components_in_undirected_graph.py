from typing import List


class Solution:
    # TODO: Union-find
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        pass


s = Solution()
print(s.countComponents(5, edges=[[0, 1], [1, 2], [3, 4]]))
print(s.countComponents(5, edges=[[0, 1], [1, 2], [2, 3], [3, 4]]))
