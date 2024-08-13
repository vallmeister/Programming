from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.backtracking(0, candidates, target, [], ans)
        return ans

    def backtracking(self, i, candidates, target, curr_nums, ans):
        if target < 0:
            return
        elif target == 0:
            ans.append(list(curr_nums))
            return
        for j in range(i, len(candidates)):
            if j > i and candidates[j] == candidates[j - 1]:
                continue
            num = candidates[j]
            curr_nums.append(num)
            self.backtracking(j + 1, candidates, target - num, curr_nums, ans)
            curr_nums.pop()


s = Solution()
print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], target=8))
print(s.combinationSum2([2, 5, 2, 1, 2], target=5))
