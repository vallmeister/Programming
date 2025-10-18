from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        ps = [0] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                ps[i] = 1
        arr1 = sum(ps[:k - 1])
        arr2 = sum(ps[k:2 * k - 1])
        left = 0
        for right in range(k - 1, n - k):
            arr1 += ps[right]
            arr2 += ps[right + k]
            arr1 -= ps[left]
            arr2 -= ps[left + k]
            left += 1
            if arr1 >= k - 1 and arr2 >= k - 1:
                return True
        return False


s = Solution()
print(s.hasIncreasingSubarrays(nums=[2, 5, 7, 8, 9, 2, 3, 4, 3, 1], k=3))
print(s.hasIncreasingSubarrays(nums=[1, 2, 3, 4, 4, 4, 4, 5, 6, 7], k=5))
print(s.hasIncreasingSubarrays([-15, 3, 16, 0], 2))
print(s.hasIncreasingSubarrays([6, 13, -17, -20, 2], 2))
