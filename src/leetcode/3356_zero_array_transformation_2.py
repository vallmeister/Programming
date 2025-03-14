from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)
        line_sweep = [0] * (n + 1)
        k = curr = 0
        for i, num in enumerate(nums):
            curr += line_sweep[i]
            while k < m and curr < num:
                l, r, val = queries[k]
                k += 1
                if l <= i <= r:
                    curr += val
                    line_sweep[r + 1] -= val
                elif i < l:
                    line_sweep[l] += val
                    line_sweep[r + 1] -= val
            if curr < num:
                return -1
        return k


s = Solution()
print(s.minZeroArray(nums=[2, 0, 2], queries=[[0, 2, 1], [0, 2, 1], [1, 1, 3]]))
print(s.minZeroArray(nums=[4, 3, 2, 1], queries=[[1, 3, 2], [0, 2, 1]]))
