class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_overall = 0
        curr_ones = 0
        last_ones = -1

        for num in nums:
            if num == 1:
                curr_ones += 1
            else:
                max_overall = max(max_overall, curr_ones + last_ones + 1)
                last_ones = curr_ones
                curr_ones = 0

        return max(max_overall, curr_ones + last_ones + 1)

    def find_max_consecutive_ones_sliding_window(self, nums):
        i = 0
        j = 0
        zeros = 0
        max_so_far = 0
        while j < len(nums):
            if nums[j] == 0:
                zeros += 1
            while zeros >= 2:
                if nums[i] == 0:
                    zeros -= 1
                i += 1
            max_so_far = max(max_so_far, j - i + 1)
            j += 1

        return max_so_far


s = Solution()
print(s.findMaxConsecutiveOnes([1, 0, 1, 1, 0]))
print(s.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
print(s.findMaxConsecutiveOnes([1, 1, 0, 1]))
