import math
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_array = sorted(arr)
        ranks = {}
        curr_rank = 0
        curr_num = -math.inf
        for num in sorted_array:
            if num == curr_num:
                continue
            curr_rank += 1
            ranks[num] = curr_rank
            curr_num = num
        return [ranks[num] for num in arr]


s = Solution()
print(s.arrayRankTransform([40, 10, 20, 30]))
