from collections import Counter
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        for s in arr:
            if count[s] > 1:
                continue
            else:
                k -= 1
            if k == 0:
                return s
        return ""


sol = Solution()
print(sol.kthDistinct(arr=["d", "b", "c", "b", "c", "a"], k=2))
