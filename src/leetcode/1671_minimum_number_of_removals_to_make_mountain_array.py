from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [0] * n
        lds = [0] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)
        for i in reversed(range(n)):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    lds[i] = max(lds[i], lds[j] + 1)
        removals = n
        for i in range(n):
            if lis[i] > 0 and lds[i] > 0:
                removals = min(removals, n - (lis[i] + lds[i] + 1))
        return removals


s = Solution()
print(s.minimumMountainRemovals([1, 3, 1]))
print(s.minimumMountainRemovals([2, 1, 1, 5, 6, 2, 3, 1]))
print(s.minimumMountainRemovals([9, 8, 1, 7, 6, 5, 4, 3, 2, 1]))
print(s.minimumMountainRemovals([4, 5, 13, 17, 1, 7, 6, 11, 2, 8, 10, 15, 3, 9, 12, 14, 16]))
