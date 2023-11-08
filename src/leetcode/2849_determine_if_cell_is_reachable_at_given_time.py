class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t == 1:
            return False
        mind_dist = max(abs(sx - fx), abs(sy - fy))
        if mind_dist > t:
            return False
        else:
            return True


s = Solution()
print(s.isReachableAtTime(2, sy=4, fx=7, fy=7, t=6))
print(s.isReachableAtTime(sx=3, sy=1, fx=7, fy=3, t=3))
print(s.isReachableAtTime(870744264, 360311537, 820090827, 890107308, 274809225))
print(s.isReachableAtTime(1, 2, 1, 2, 1))
print(s.isReachableAtTime(1, 1, 1, 1, 3))
