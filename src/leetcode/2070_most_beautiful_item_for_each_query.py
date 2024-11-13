import bisect
from collections import defaultdict
from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        best_items = []
        pp, pb = items[0]
        for p, b in items[1:]:
            if pb >= b:
                continue
            best_items.append((pp, pb))
            pp, pb = p, b
        best_items.append((pp, pb))
        ans = []
        for q in queries:
            left = 0
            right = len(best_items) - 1
            cb = 0
            while left <= right:
                mid = (left + right) // 2
                p, b = best_items[mid]
                if p > q:
                    right = mid - 1
                else:
                    cb = max(cb, b)
                    left = mid + 1
            ans.append(cb)
        return ans


s = Solution()
print(s.maximumBeauty([[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [1, 2, 3, 4, 5, 6]))
