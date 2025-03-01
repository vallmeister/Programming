from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = {}
        ans = 0
        for i in reversed(range(n)):
            a = arr[i]
            for j in range(i + 1, n):
                b = arr[j]
                if (b, a + b) in dp:
                    dp[(a, b)] = 1 + dp[(b, a + b)]
                else:
                    dp[(a, b)] = 2
                if dp[(a, b)] >= 3:
                    ans = max(ans, dp[(a, b)])
        return ans


s = Solution()
print(s.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))
print(s.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]))
