from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        monotonic_stack = []
        for i in range(n):
            while monotonic_stack and temperatures[monotonic_stack[-1]] < temperatures[i]:
                day = monotonic_stack.pop()
                ans[day] = i - day
            monotonic_stack.append(i)
        return ans


s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(s.dailyTemperatures([30, 40, 50, 60]))
print(s.dailyTemperatures([30, 60, 90]))
