class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = (n + 1) * n // 2
        for num in nums:
            s -= num
        return s
