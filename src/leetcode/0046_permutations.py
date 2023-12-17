from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backtrack(curr_permutation, visited):
            if len(curr_permutation) == n:
                ans.append(list(curr_permutation))
            for num in nums:
                if num in visited:
                    continue
                curr_permutation.append(num)
                visited.add(num)
                backtrack(curr_permutation, visited)
                curr_permutation.pop()
                visited.discard(num)

        backtrack([], set())
        return ans


s = Solution()
print(s.permute([1, 2, 3]))
print(s.permute([0, 1]))
