from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)

        max_ramp = 0
        for i in reversed(range(n)):
            while stack and nums[stack[-1]] <= nums[i]:
                j = stack.pop()
                max_ramp = max(max_ramp, i - j)
        return max_ramp

    def max_width_ramp_sorting(self, nums):
        nums = list(sorted(enumerate(nums), key=lambda x: x[1]))
        max_ramp = 0
        min_idx, _ = nums[0]
        for idx, _ in nums[1:]:
            if idx > min_idx:
                max_ramp = max(max_ramp, idx - min_idx)
            else:
                min_idx = idx
        return max_ramp
