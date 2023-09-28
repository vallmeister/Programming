from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        i = 0
        j = n - 1
        for num in nums:
            if num % 2 == 0:
                ans[i] = num
                i += 1
            else:
                ans[j] = num
                j -= 1
        return ans

    def sort_array_by_parity_inplace(self, nums):
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] % 2 == 1 and nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
            while i < len(nums) and nums[i] % 2 == 0:
                i += 1
            while j > 0 and nums[j] % 2 == 1:
                j -= 1
        return nums


s = Solution()
print(s.sort_array_by_parity_inplace([3, 1, 2, 4]))
print(s.sort_array_by_parity_inplace([0]))
print(s.sort_array_by_parity_inplace([0, 2]))
