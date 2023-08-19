from typing import List
from copy import deepcopy


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def generate(permutation, numbers):
            if not numbers:
                result.append(deepcopy(permutation))
            else:
                for i in range(len(numbers)):
                    n = numbers.pop(i)
                    permutation.append(n)
                    generate(permutation, numbers)
                    permutation.pop()
                    numbers.insert(i, n)

        generate([], nums)
        return result


s = Solution()
print(s.permute([1, 2, 3]))
print(s.permute([0, 1]))
