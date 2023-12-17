from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)

        def backtrack(curr_sum, curr_numbers, start):
            if curr_sum == target:
                ans.append(list(curr_numbers))
                return
            elif curr_sum > target:
                return
            for i in range(start, n):
                num = candidates[i]
                curr_numbers.append(num)
                backtrack(curr_sum + num, curr_numbers, i)
                curr_numbers.pop()

        backtrack(0, [], 0)
        return ans


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
print(s.combinationSum([2, 3, 5], 8))
print(s.combinationSum([2], 1))
