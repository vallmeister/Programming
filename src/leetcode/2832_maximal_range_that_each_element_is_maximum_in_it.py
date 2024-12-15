from typing import List


class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        n = len(nums)
        next_greater = [n] * n
        prev_grater = [-1] * n

        mono_stack = []
        for i in range(n):
            while mono_stack and nums[i] > nums[mono_stack[-1]]:
                next_greater[mono_stack.pop()] = i
            mono_stack.append(i)

        mono_stack = []
        for i in reversed(range(n)):
            while mono_stack and nums[i] > nums[mono_stack[-1]]:
                prev_grater[mono_stack.pop()] = i
            mono_stack.append(i)

        return [next_greater[i] - prev_grater[i] - 1 for i in range(n)]
