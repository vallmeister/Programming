from collections import defaultdict
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = ans = 0
        freq = defaultdict(int)
        score = 0
        for num in nums:
            freq[num] += 1
            score += num
            while freq[num] > 1:
                left_num = nums[left]
                score -= left_num
                freq[left_num] -= 1
                left += 1
            ans = max(ans, score)
        return ans


s = Solution()
print(s.maximumUniqueSubarray([4, 2, 4, 5, 6]))
print(s.maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]))
