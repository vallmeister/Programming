from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            num = str(num)
            for digit in '987654321':
                if digit in num:
                    ans += int(digit * len(num))
                    break
        return ans


s = Solution()
print(s.sumOfEncryptedInt([10, 21, 31]))
