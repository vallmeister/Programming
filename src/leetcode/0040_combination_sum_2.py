from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        candidates.sort()

        def backtrack(start, curr_nums, curr_sum):
            if curr_sum == target:
                ans.add(tuple(curr_nums))
                return
            elif curr_sum > target:
                return
            next_numbers = set()
            for i in range(start, len(candidates)):
                num = candidates[i]
                if num in next_numbers:
                    continue
                curr_nums.append(num)
                backtrack(i + 1, curr_nums, curr_sum + num)
                curr_nums.pop()
                next_numbers.add(num)

        backtrack(0, [], 0)
        return [list(tpl) for tpl in ans]


s = Solution()
print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], target=8))
print(s.combinationSum2([2, 5, 2, 1, 2], target=5))
