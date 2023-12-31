from collections import Counter, defaultdict
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        num_count = Counter(nums)

        def backtrack(curr_permutation, curr_count):
            if len(curr_permutation) == len(nums):
                ans.add(tuple(curr_permutation))
                return
            # TODO: improve with trick
            for num in nums:
                if num_count[num] == curr_count[num]:
                    continue
                curr_permutation.append(num)
                curr_count[num] += 1
                backtrack(curr_permutation, curr_count)
                curr_count[num] -= 1
                curr_permutation.pop()

        backtrack([], defaultdict(int))
        return [list(tpl) for tpl in ans]


s = Solution()
print(s.permuteUnique([1, 1, 2]))
print(s.permuteUnique([1, 2, 3]))
