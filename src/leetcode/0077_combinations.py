from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(start, curr_combination):
            if len(curr_combination) == k:
                ans.append(list(curr_combination))
                return
            for num in range(start, n + 1):
                curr_combination.append(num)
                backtrack(num + 1, curr_combination)
                curr_combination.pop()

        backtrack(1, [])
        return ans


s = Solution()
print(s.combine(4, 2))
print(s.combine(1, 1))
print(s.combine(3, 3))
