from typing import List


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        ans = 0

        def strictly_increasing(arr):
            if not arr:
                return True
            prev = arr[0]
            for element in arr[1:]:
                if element <= prev:
                    return False
                prev = element
            return True

        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if strictly_increasing(nums[:i] + nums[j + 1:]):
                    ans += 1
        return ans


s = Solution()
print(s.incremovableSubarrayCount([1, 2, 3, 4]))
print(s.incremovableSubarrayCount([6, 5, 7, 8]))
print(s.incremovableSubarrayCount([8, 7, 6, 6]))
print(s.incremovableSubarrayCount([2, 1, 2, 3, 4]))
