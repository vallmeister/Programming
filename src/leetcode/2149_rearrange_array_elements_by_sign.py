from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []
        pos = 0
        while nums[pos] < 0:
            pos += 1
        neg = 0
        while nums[neg] >= 0:
            neg += 1
        n = len(nums)
        while len(ans) < n:
            ans.append(nums[pos])
            pos += 1
            ans.append(nums[neg])
            neg += 1
            while pos < n and nums[pos] < 0:
                pos += 1
            while neg < n and nums[neg] > 0:
                neg += 1
        return ans


print(Solution().rearrangeArray([3, 1, -2, -5, 2, -4]))
