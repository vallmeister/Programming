from collections import defaultdict
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        out_degree = defaultdict(int)
        for start, dest in paths:
            out_degree[start] += 1
            out_degree[dest] += 0
        for city, degree in out_degree.items():
            if degree == 0:
                return city
        return ''


s = Solution()
print(s.destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
print(s.destCity([["B", "C"], ["D", "B"], ["C", "A"]]))
print(s.destCity([["A", "Z"]]))
