from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dominant = nums[0]
        count = 1
        for num in nums[1:]:
            if dominant == num:
                count += 1
            else:
                count -= 1
            if count == 0:
                dominant = num
                count = 1

        n = len(nums)
        freq = [0] * (n + 1)
        for i, num in enumerate(nums):
            freq[i + 1] = freq[i]
            if dominant == num:
                freq[i + 1] += 1

        for i in range(1, n):
            if freq[i] > i // 2 and freq[-1] - freq[i] > (n - i) // 2:
                return i - 1
        return -1


s = Solution()
print(s.minimumIndex([1, 2, 2, 2]))
print(s.minimumIndex([2, 1, 3, 1, 1, 1, 7, 1, 2, 1]))
print(s.minimumIndex([3, 3, 3, 3, 7, 2, 2]))
