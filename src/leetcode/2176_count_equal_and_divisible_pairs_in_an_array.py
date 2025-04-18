import math
from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        indices = defaultdict(list)
        for i in range(len(nums)):
            indices[nums[i]].append(i)
        divisors = self.get_divisors(k)
        for index_list in indices.values():
            prev = defaultdict(int)
            for i in index_list:
                gcd = self.gcd(i, k)
                target = k // gcd
                ans += prev[target]
                for d in divisors:
                    if i % d == 0:
                        prev[d] += 1
        return ans

    def gcd(self, a, b):
        while b > 0:
            if a < b:
                a, b = b, a
                continue
            a -= b
        return a

    def get_divisors(self, n):
        divisors = []
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return divisors


s = Solution()
print(s.countPairs(nums=[3, 1, 2, 2, 2, 1, 3], k=2))
