from heapq import heappush, heappop
from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10 ** 9 + 7
        ps = [0] * (n + 1)
        for i in range(1, n + 1):
            ps[i] = ps[i - 1] + nums[i - 1]
        sas = []
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                heappush(sas, - (ps[j] - ps[i - 1]))
                while len(sas) > right:
                    heappop(sas)
        ans = 0
        for i in reversed(range(right)):
            curr_sas = heappop(sas)
            if i >= left - 1:
                ans -= curr_sas
                ans %= MOD
        return ans


s = Solution()
print(s.rangeSum(nums=[1, 2, 3, 4], n=4, left=1, right=5))
print(s.rangeSum(nums=[1, 2, 3, 4], n=4, left=3, right=4))
