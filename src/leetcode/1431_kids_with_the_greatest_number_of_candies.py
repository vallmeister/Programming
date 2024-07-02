from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        ans = []
        for c in candies:
            ans.append(c + extraCandies >= max_candies)
        return ans
