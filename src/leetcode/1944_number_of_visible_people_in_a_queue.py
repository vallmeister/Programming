from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        mono_stack = []
        for i in reversed(range(n)):
            to_the_right = 0
            while mono_stack:
                to_the_right += 1
                if heights[mono_stack[-1]] < heights[i]:
                    mono_stack.pop()
                else:
                    break
            ans[i] = to_the_right
            mono_stack.append(i)
        return ans


s = Solution()
print(s.canSeePersonsCount([10, 6, 8, 5, 11, 9]))
print(s.canSeePersonsCount([5, 1, 2, 3, 10]))
