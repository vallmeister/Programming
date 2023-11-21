from collections import defaultdict
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        ans = 0
        n = len(nums)
        differences = defaultdict(int)
        for i in range(n):
            diff = nums[i] - int(str(nums[i])[::-1])
            differences[diff] += 1
        for pairs in differences.values():
            ans += pairs * (pairs - 1) // 2
        return ans % MOD


s = Solution()
print(s.countNicePairs([42, 11, 1, 97]))
print(s.countNicePairs([13, 10, 35, 24, 76]))
