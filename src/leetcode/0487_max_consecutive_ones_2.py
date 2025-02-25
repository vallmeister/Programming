class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        n = len(nums)
        zeroes = 0
        left = 0
        ans = 0
        for right in range(n):
            zeroes += 1 - nums[right]
            while zeroes > 1:
                zeroes -= (1 - nums[left])
                left += 1
            ans = max(ans, right - left + 1)
        return ans

    def follow_up(self, nums):
        n = len(nums)
        prev = pprev = -1
        ans = 0
        for i in range(n):
            if nums[i] == 0:
                pprev = prev
                prev = i
            ans = max(ans, i - pprev)
        return ans


s = Solution()
print(s.findMaxConsecutiveOnes([1, 0, 1, 1, 0]))
print(s.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
print(s.findMaxConsecutiveOnes([1, 1, 0, 1]))
