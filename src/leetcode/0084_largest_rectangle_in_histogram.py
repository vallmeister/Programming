from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        next_smaller = [n] * n
        mono_stack = []
        for i in range(n):
            while mono_stack and heights[i] < heights[mono_stack[-1]]:
                next_smaller[mono_stack.pop()] = i
            mono_stack.append(i)

        prev_smaller = [-1] * n
        mono_stack = []
        for i in reversed(range(n)):
            while mono_stack and heights[i] < heights[mono_stack[-1]]:
                prev_smaller[mono_stack.pop()] = i
            mono_stack.append(i)

        ans = 0
        for i in range(n):
            ans = max(ans, (next_smaller[i] - prev_smaller[i] - 1) * heights[i])
        return ans


s = Solution()
print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(s.largestRectangleArea([2, 4]))
