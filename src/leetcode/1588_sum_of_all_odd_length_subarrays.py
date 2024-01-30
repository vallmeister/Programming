from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ps = [0] * (n + 1)
        for i in range(1, n + 1):
            ps[i] = ps[i - 1] + arr[i - 1]
        ans = ps[-1]
        for i in range(3, n + 1, 2):
            for j in range(n + 1):
                if j - i < 0:
                    continue
                ans += ps[j] - ps[j - i]
        return ans


s = Solution()
print(s.sumOddLengthSubarrays([1, 4, 2, 5, 3]))
print(s.sumOddLengthSubarrays([1, 2]))
print(s.sumOddLengthSubarrays([10, 11, 12]))
