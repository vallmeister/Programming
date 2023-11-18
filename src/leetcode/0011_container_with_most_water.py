from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        n = len(height)
        i = 0
        j = n - 1
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(s.maxArea([1, 1]))
print(s.maxArea([1, 2, 4, 3]))
