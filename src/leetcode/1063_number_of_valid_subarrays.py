from typing import List


class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        next_smaller = [n] * n
        mono_stack = []
        for i in range(n):
            while mono_stack and nums[mono_stack[-1]] > nums[i]:
                idx = mono_stack.pop()
                next_smaller[idx] = i
            mono_stack.append(i)
        ans = 0
        for i in range(n):
            ans += next_smaller[i] - i
        return ans


s = Solution()
print(s.validSubarrays([1, 4, 2, 5, 3]))
print(s.validSubarrays([3, 2, 1]))
print(s.validSubarrays([2, 2, 2]))
