from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        exponent = 0
        for i in range(1, n + 1):
            if i == 2 ** exponent:
                ans[i] = 1
                exponent += 1
            else:
                idx = i - 2 ** (exponent - 1)
                ans[i] = ans[idx] + 1
        return ans


s = Solution()
print(s.countBits(2))
print(s.countBits(5))
