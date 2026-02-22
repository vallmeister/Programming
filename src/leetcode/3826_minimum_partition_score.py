import math
from typing import List


# WTF?
class Solution:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ps = self.get_prefix_sum(nums)

        # prev[j] = cost of grouping the first j + 1 elements, initially for 1 group
        prev = [0] + [self.get_cost(0, j, ps) for j in range(1, n + 1)]

        for groups in range(2, k + 1):
            curr = [math.inf] * (n + 1)
            self.divide_and_conquer(groups, n, groups - 1, n - 1, ps, prev, curr)
            prev = curr

        return prev[n]

    def get_prefix_sum(self, nums):
        n = len(nums)
        ps = [0] * (n + 1)
        for i in range(n):
            ps[i + 1] = ps[i] + nums[i]
        return ps

    def get_cost(self, i, j, ps):
        sm = ps[j] - ps[i]
        return sm * (sm + 1) // 2

    def divide_and_conquer(self, left, right, opt_l, opt_r, ps, prev, curr):
        if left > right:
            return
        mid = (left + right) // 2

        best_val = math.inf
        best_j = -1

        for j in range(opt_l, min(opt_r, mid - 1) + 1):
            candidate = prev[j] + self.get_cost(j, mid, ps)
            if candidate < best_val:
                best_val = candidate
                best_j = j

        curr[mid] = best_val
        if best_j == -1:
            return
        self.divide_and_conquer(left, mid - 1, opt_l, best_j, ps, prev, curr)
        self.divide_and_conquer(mid + 1, right, best_j, opt_r, ps, prev, curr)


s = Solution()
print(s.minPartitionScore(nums=[5, 1, 2, 1], k=2))
print(s.minPartitionScore(nums=[1, 2, 3, 4], k=1))
print(s.minPartitionScore(nums=[1, 1, 1], k=3))
