import math


class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        limit = int(math.sqrt(r))
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        special = 0
        for i in range(2, limit + 1):
            if sieve[i]:
                for j in range(i * i, limit + 1, i):
                    sieve[j] = False
                if l <= i * i <= r:
                    special += 1
        return r - l + 1 - special


s = Solution()
print(s.nonSpecialCount(400882894, 845316433))
