from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        colors += '*'
        neededTime.append(0)
        n = len(colors)
        ans = 0
        prev_color = colors[0]
        curr_total_time = neededTime[0]
        max_time = neededTime[0]
        for i in range(1, n):
            color = colors[i]
            time = neededTime[i]
            if color == prev_color:
                curr_total_time += time
                max_time = max(max_time, time)
            else:
                ans += curr_total_time - max_time
                curr_total_time = time
                max_time = time
            prev_color = color
        return ans


s = Solution()
print(s.minCost("abaac", neededTime=[1, 2, 3, 4, 5]))
print(s.minCost("abc", neededTime=[1, 2, 3]))
print(s.minCost("aabaa", neededTime=[1, 2, 3, 4, 1]))
