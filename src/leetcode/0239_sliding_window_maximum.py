from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        j = k
        curr_sum = sum(nums[i:k])
        max_sum = curr_sum
        result = [max_sum]
        while j < len(nums):
            curr_sum -= nums[i]
            curr_sum += nums[j]
            i += 1
            j += 1
            max_sum = max(max_sum, curr_sum)
            result.append(max_sum)
        return result


s = Solution()
print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], k=3))
print(s.maxSlidingWindow([1], k=1))
