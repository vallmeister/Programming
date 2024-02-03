from functools import cache
from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)

        @cache
        def recursive(idx, curr_len, curr_max):
            if idx == n:
                return curr_len * curr_max
            elif curr_len == k:
                return curr_len * curr_max + recursive(idx, 0, 0)
            elif curr_len == 0:
                return recursive(idx + 1, 1, arr[idx])
            else:
                return max(recursive(idx + 1, curr_len + 1, max(curr_max, arr[idx])),
                           curr_len * curr_max + recursive(idx, 0, 0))

        return recursive(0, 0, 0)


s = Solution()
print(s.maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], k=3))
print(s.maxSumAfterPartitioning([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], k=4))
print(s.maxSumAfterPartitioning([1], k=1))
