from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        total = mn = mx = 0
        for d in differences:
            total += d
            mn = min(mn, total)
            mx = max(mx, total)
        return max(0,(upper - lower) - (mx - mn) + 1)


s = Solution()
print(s.numberOfArrays(differences=[1, -3, 4], lower=1, upper=6))
print(s.numberOfArrays(differences=[3, -4, 5, 1, -2], lower=-4, upper=5))
print(s.numberOfArrays(differences=[4, -7, 2], lower=3, upper=6))
