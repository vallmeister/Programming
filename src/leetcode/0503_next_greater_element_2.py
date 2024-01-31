from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        ms = []
        nums *= 2
        for i, num in enumerate(nums):
            while ms and nums[ms[-1]] < num:
                idx = ms.pop()
                ans[idx] = num
            if i < n:
                ms.append(i)
        return ans


s = Solution()
print(s.nextGreaterElements([1, 2, 1]))
print(s.nextGreaterElements([1, 2, 3, 4, 3]))
