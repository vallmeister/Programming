from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        ps = [0] * n
        ps[0] = nums[0]
        for i in range(1, n):
            ps[i] = ps[i - 1] + nums[i]
        total = ps[-1]
        ans = 0
        for i in range(n - 1):
            if ps[i] >= total - ps[i]:
                ans += 1
        return ans


s = Solution()
print(s.waysToSplitArray([10, 4, -8, 7]))
print(s.waysToSplitArray([2, 3, 1, 0]))
