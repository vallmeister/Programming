class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_so_far = 0
        max_overall = 0
        for num in nums:
            if num == 0:
                max_so_far = 0
            else:
                max_so_far += 1
                max_overall = max(max_overall, max_so_far)
        return max_overall


s = Solution()
print(s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
print(s.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
