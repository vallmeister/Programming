from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        return len(set(cnt.values())) == len(set(cnt.keys()))


s = Solution()
print(s.uniqueOccurrences([1, 2, 2, 1, 1, 3]))
print(s.uniqueOccurrences([1, 2]))
print(s.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
