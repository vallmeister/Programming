from collections import Counter
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        stack = sorted(counter.values(), reverse=True)
        while stack and stack[-1] <= k:
            k -= stack.pop()
        return len(stack)


s = Solution()
print(s.findLeastNumOfUniqueInts([5, 5, 4], 1))
print(s.findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], k=3))
