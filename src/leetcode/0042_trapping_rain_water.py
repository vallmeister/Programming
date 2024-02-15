class Solution:
    def trap(self, height: list[int]) -> int:
        ans = 0
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i - 1])
        for i in reversed(range(n - 1)):
            right_max[i] = max(right_max[i + 1], height[i + 1])
        for i in range(n):
            ans += max(min(left_max[i], right_max[i]) - height[i], 0)
        return ans


s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(s.trap([4, 2, 0, 3, 2, 5]))
print(s.trap([4, 2, 3]))
