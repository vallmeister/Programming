from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev = '*'
        ans = curr_time = 0
        for i, color in enumerate(colors):
            if prev == color:
                ans += min(curr_time, neededTime[i])
                curr_time = max(curr_time, neededTime[i])
            else:
                prev = color
                curr_time = neededTime[i]
        return ans


s = Solution()
print(s.minCost("abaac", neededTime=[1, 2, 3, 4, 5]))
print(s.minCost("abc", neededTime=[1, 2, 3]))
print(s.minCost("aabaa", neededTime=[1, 2, 3, 4, 1]))
