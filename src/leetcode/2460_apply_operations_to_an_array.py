from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        ans = []
        for i in range(n):
            if nums[i] != 0:
                ans.append(nums[i])
        while len(ans) < n:
            ans.append(0)
        return ans


s = Solution()
print(s.applyOperations([1, 2, 2, 1, 1, 0]))
print(s.applyOperations([0, 1]))
