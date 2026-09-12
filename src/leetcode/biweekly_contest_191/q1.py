from collections import defaultdict


class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        ans = 0
        count = defaultdict(list)
        for i, num in enumerate(nums):
            count[num].append(i)

        for indices in count.values():
            if len(indices) < 3:
                continue
            i, j, k = indices
            if j - i != k - j:
                continue
            ans += 1

        return ans


s = Solution()
print(s.countSpecialIntegers(nums=[1, 8, 1, 5, 1, 5, 8, 5]))
