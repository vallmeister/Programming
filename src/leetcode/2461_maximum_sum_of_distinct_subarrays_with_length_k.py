from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        key_sum = window = 0
        counter = {}
        for num in nums[:k - 1]:
            if num not in counter:
                counter[num] = 0
                key_sum += num
            counter[num] += 1
            window += num
        for right in range(k - 1, n):
            num = nums[right]
            if num not in counter:
                counter[num] = 0
                key_sum += num
            counter[num] += 1
            window += num
            if key_sum == window:
                ans = max(ans, window)

            num = nums[right - k + 1]
            counter[num] -= 1
            window -= num
            if counter[num] == 0:
                del counter[num]
                key_sum -= num
        return ans


s = Solution()
print(s.maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3))
print(s.maximumSubarraySum([1, 1, 1, 7, 8, 9], 3))
