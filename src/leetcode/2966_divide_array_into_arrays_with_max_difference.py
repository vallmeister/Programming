from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        curr_group = []
        for i in range(n + 1):
            if i % 3 == 0:
                if curr_group and max(curr_group) - min(curr_group) > k:
                    return []
                elif i > 0:
                    ans.append(curr_group)
                curr_group = []
            if i < n:
                curr_group.append(nums[i])
        return ans
