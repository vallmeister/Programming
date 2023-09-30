from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        n = len(nums)
        min_array = [-1] * n
        min_array[0] = nums[0]
        for i in range(1, n):
            min_array[i] = min(min_array[i - 1], nums[i])
        stack = []
        for j in range(n - 1, -1, -1):
            if nums[j] <= min_array[j]:
                continue
            while stack and stack[-1] <= min_array[j]:
                stack.pop()
            if stack and stack[-1] < nums[j]:
                return True
            stack.append(nums[j])
        return False


s = Solution()
print(s.find132pattern([1, 2, 3, 4]))
print(s.find132pattern([3, 1, 4, 2]))
print(s.find132pattern([-1, 3, 2, 0]))
print(s.find132pattern([3, 5, 0, 3, 4]))
