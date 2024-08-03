from collections import Counter
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        c1 = Counter(arr)
        c2 = Counter(target)
        return all(c2[k] == v for k, v in c1.items())
