from collections import defaultdict


class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        ans = 0
        count = defaultdict(list)
        for i, num in enumerate(nums):
            count[num].append(i)

        for indices in count.values():
            n = len(indices)
            if n < 3:
                continue
            d = indices[1] - indices[0]
            for i in range(2, n):
                if indices[i] - indices[i - 1] != d:
                    break
            else:
                ans += 1

        return ans