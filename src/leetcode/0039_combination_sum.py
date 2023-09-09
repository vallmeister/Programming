from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def generate_combination(curr_combination, curr_sum, curr_candidates):
            for i in range(len(curr_candidates)):
                tmp_sum = curr_sum + curr_candidates[i]
                if tmp_sum == target:
                    curr_combination.append(curr_candidates[i])
                    result.append(list(curr_combination))
                    curr_combination.pop()
                elif tmp_sum > target:
                    break
                elif tmp_sum < target:
                    curr_combination.append(curr_candidates[i])
                    generate_combination(curr_combination, tmp_sum, curr_candidates[i:])
                    curr_combination.pop()

        generate_combination([], 0, candidates)
        return result


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
print(s.combinationSum([2, 3, 5], 8))
print(s.combinationSum([2], 1))
