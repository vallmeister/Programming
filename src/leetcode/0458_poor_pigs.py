import math


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        attempts = minutesToTest / minutesToDie + 1
        pigs = math.log(buckets, attempts)
        pigs = round(pigs, 2)
        pigs = math.ceil(pigs)
        return pigs


s = Solution()
print(s.poorPigs(4, 15, 15))
print(s.poorPigs(4, 15, 30))
print(s.poorPigs(1, 15, 30))
print(s.poorPigs(125, 1, 4))
