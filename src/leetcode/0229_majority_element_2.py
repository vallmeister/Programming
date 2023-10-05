from collections import Counter
from typing import List


class Solution:
    # TODO: Boyer-Moore majority voting
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        return [num for num, occurrences in counter.items() if occurrences > n // 3]


s = Solution()
print(s.majorityElement([3, 2, 3]))
print(s.majorityElement([1]))
print(s.majorityElement([1, 2]))
