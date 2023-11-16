from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []
        for idx, num in enumerate(nums):
            if num[idx] == '1':
                ans.append('0')
            else:
                ans.append('1')
        return ''.join(ans)


s = Solution()
print(s.findDifferentBinaryString(["01", "10"]))
print(s.findDifferentBinaryString(["00", "01"]))
print(s.findDifferentBinaryString(["111", "011", "001"]))
