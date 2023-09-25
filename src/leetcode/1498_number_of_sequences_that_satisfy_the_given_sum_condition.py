from typing import List


# TODO: fix
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[0] + nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        possible_sequences = 2 ** right - 1
        right_most = right - 1
        left = 0
        while left < right:
            mid = (left + right) // 2
            if nums[mid] + nums[right_most] <= target:
                left = mid + 1
            else:
                right = mid
        bad_sequences = 2 ** (right_most - left) - 1
        return possible_sequences - bad_sequences


s = Solution()
print(s.numSubseq([3, 5, 6, 7], target=9))
print(s.numSubseq([3, 3, 6, 8], target=10))
print(s.numSubseq([2, 3, 3, 4, 6, 7], target=12))
