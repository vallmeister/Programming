from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        colors *= 2
        left_alternating = [0] * 2 * n
        right_alternating = [0] * 2 * n
        left_alternating[0] = right_alternating[-1] = 1
        for i in range(1, 2 * n):
            left_alternating[i] = colors[i] ^ colors[i - 1]
        for i in reversed(range(2 * n - 1)):
            right_alternating[i] = colors[i] ^ colors[i + 1]
        window = ans = 0
        for right in range(k - 1):
            window += left_alternating[right]
        left = 0
        for right in range(k - 1, n + k - 1):
            window += left_alternating[right]
            if window == k:
                ans += 1
            window -= right_alternating[left]
            left += 1
        return ans


s = Solution()
print(s.numberOfAlternatingGroups([0, 1, 0, 0, 1, 0, 1], 6))
