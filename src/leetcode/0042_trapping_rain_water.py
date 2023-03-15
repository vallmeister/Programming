class Solution:
    def trap(self, height: list[int]) -> int:
        water = 0
        left = height[0]
        for h in height[1:]:
            if h > left:
                left = h
            else:
                water += left - h
        return water


s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(s.trap([4, 2, 0, 3, 2, 5]))
