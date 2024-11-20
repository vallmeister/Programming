from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        window = 0
        right = 0
        for _ in range(abs(k)):
            window += code[right]
            right += 1
        for _ in range(n):
            window += code[right]
            window -= code[(right - abs(k) + n) % n]
            if k > 0:
                ans[(right - k + n) % n] = window
            elif k < 0:
                ans[(right + 1) % n] = window
            right += 1
            right %= n
        return ans


s = Solution()
print(s.decrypt([5, 7, 1, 4], 3))
print(s.decrypt([1, 2, 3, 4], 0))
print(s.decrypt([2, 4, 9, 3], -2))
