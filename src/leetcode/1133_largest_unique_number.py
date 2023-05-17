from collections import defaultdict


class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        table = defaultdict(list)
        for num in nums:
            table[num].append(num)
        max_so_far = -1
        for num_list in table.values():
            if len(num_list) > 1:
                continue
            max_so_far = max(max_so_far, num_list[0])
        return max_so_far


s = Solution()
print(s.largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 1]))
print(s.largestUniqueNumber([9, 9, 8, 8]))
