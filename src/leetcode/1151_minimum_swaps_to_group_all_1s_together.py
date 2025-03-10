from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ans = n = len(data)
        k = sum(data)
        if k == 0:
            return 0
        window = sum(data[:k - 1])
        left = 0
        for right in range(k - 1, n):
            window += data[right]
            ans = min(ans, k - window)
            window -= data[left]
            left += 1
        return ans


s = Solution()
print(s.minSwaps([1, 0, 1, 0, 1]))
print(s.minSwaps([0, 0, 0, 1, 0]))
print(s.minSwaps([1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1]))
print(s.minSwaps([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
