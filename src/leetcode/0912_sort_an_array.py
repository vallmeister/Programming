from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums
        left = self.sortArray(nums[:n // 2])
        right = self.sortArray(nums[n // 2:])
        result = []
        i = j = 0
        while len(result) < n:
            if i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            elif i < len(left):
                result.append(left[i])
                i += 1
            elif j < len(right):
                result.append(right[j])
                j += 1
        return result


s = Solution()
print(s.sortArray([5, 2, 3, 1]))
print(s.sortArray([5, 1, 1, 2, 0, 0]))
