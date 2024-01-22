from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counter = [0] * (n + 1)
        ans = []
        for num in nums:
            counter[num] += 1
            if counter[num] == 2:
                ans.append(num)
        for i in range(1, n + 1):
            if counter[i] == 0:
                ans.append(i)
        return ans


s = Solution()
print(s.findErrorNums([1, 2, 2, 4]))
print(s.findErrorNums([1, 1]))
