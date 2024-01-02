from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        child = 0
        cookie = 0
        ans = 0
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                ans += 1
                child += 1
                cookie += 1
            else:
                cookie += 1

        return ans


sol = Solution()
print(sol.findContentChildren([1, 2, 3], s=[1, 1]))
print(sol.findContentChildren([1, 2], s=[1, 2, 3]))
