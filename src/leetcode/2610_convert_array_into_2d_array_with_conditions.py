from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        m = max(count.values())
        ans = [[] for _ in range(m)]
        for num in nums:
            count[num] -= 1
            row = count[num]
            ans[row].append(num)
        return ans


s = Solution()
print(s.findMatrix([1, 3, 4, 1, 2, 3, 1]))
print(s.findMatrix([1, 2, 3, 4]))
