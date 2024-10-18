from functools import reduce
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_value = reduce(lambda a, b: a | b, nums)
        n = len(nums)

        def backtracking(curr, i):
            tmp = 0
            if curr == max_value:
                tmp += 1
            for j in range(i, n):
                tmp += backtracking(curr | nums[j], j + 1)
            return tmp

        return backtracking(0, 0)

    def count_max_or_subsets_iterative(self, nums):
        n = len(nums)
        max_value = reduce(lambda a, b: a | b, nums)
        ans = 0
        stack = [(0, 0)]
        while stack:
            curr, i = stack.pop()
            if curr == max_value:
                ans += 1
            for j in range(i, n):
                stack.append((curr | nums[j], j + 1))
        return ans


s = Solution()
print(s.countMaxOrSubsets([3, 1]))
print(s.countMaxOrSubsets([2, 2, 2]))
print(s.countMaxOrSubsets([3, 1, 2, 5]))
