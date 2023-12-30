from typing import List


class Solution:
    # TODO: study solution
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def sort(start):
            left = start
            right = n - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        n = len(nums)
        for j in range(n - 1, -1, -1):
            for i in range(j - 1, -1, -1):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    sort(i + 1)
                    return
        sort(0)


s = Solution()
perm = [1, 2, 3]
s.nextPermutation(perm)
print(perm)
perm = [3, 2, 1]
s.nextPermutation(perm)
print(perm)
perm = [1, 1, 5]
s.nextPermutation(perm)
print(perm)
perm = [1, 3, 2]
s.nextPermutation(perm)
print(perm)
perm = [1, 5, 1]
s.nextPermutation(perm)
print(perm)
perm = [4, 2, 0, 2, 3, 2, 0]
s.nextPermutation(perm)
print(perm)
