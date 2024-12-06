from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        curr_sum = 0
        ans = 0
        for i in range(1, n + 1):
            if i in banned:
                continue
            elif curr_sum + i > maxSum:
                break
            curr_sum += i
            ans += 1
        return ans


s = Solution()
print(s.maxCount([1, 6, 5], 5, 6))
