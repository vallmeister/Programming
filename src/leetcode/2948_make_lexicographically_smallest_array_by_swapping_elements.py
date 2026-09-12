from collections import defaultdict
from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        nums = list(sorted(enumerate(nums), key=lambda x: x[1]))
        group_indices = defaultdict(list)
        group_numbers = defaultdict(list)

        def add_element(curr_idx, curr_num, curr_group):
            group_indices[curr_group].append(curr_idx)
            group_numbers[curr_group].append(curr_num)

        group = 0
        for i, (j, num) in enumerate(nums):
            if i == 0:
                add_element(j, num, group)
                continue
            prev = nums[i - 1][1]
            if num - prev > limit:
                group += 1
            add_element(j, num, group)

        ans = [0] * len(nums)
        for g in range(group + 1):
            indices = sorted(group_indices[g])
            numbers = sorted(group_numbers[g])
            for i, num in zip(indices, numbers):
                ans[i] = num
        return ans


s = Solution()
print(s.lexicographicallySmallestArray([1, 5, 3, 9, 8], 2))
print(s.lexicographicallySmallestArray([1, 7, 6, 18, 2, 1], 3))
print(s.lexicographicallySmallestArray([1, 7, 28, 19, 10], 3))
