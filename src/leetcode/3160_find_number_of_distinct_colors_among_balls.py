from collections import defaultdict
from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_to_color = {}
        num_colors = defaultdict(int)
        distinct = 0
        ans = []
        for ball, color in queries:
            if ball in ball_to_color:
                old_color = ball_to_color[ball]
                num_colors[old_color] -= 1
                if num_colors[old_color] == 0:
                    distinct -= 1
            if num_colors[color] == 0:
                distinct += 1
            num_colors[color] += 1
            ball_to_color[ball] = color
            ans.append(distinct)
        return ans
