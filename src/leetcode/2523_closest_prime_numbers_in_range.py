from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False
        ans = [-1, -1]
        primes = []

        for i in range(right + 1):
            if not sieve[i]:
                continue
            for j in range(i * i, right + 1, i):
                sieve[j] = False
            if left <= i <= right:
                primes.append(i)

        for i in range(1, len(primes)):
            prev = primes[i - 1]
            p = primes[i]
            if ans[0] == -1 or p - prev < ans[1] - ans[0]:
                ans = [prev, p]

        return ans


s = Solution()
print(s.closestPrimes(5, 97))
print(s.closestPrimes(10 ** 5, 10 ** 6))
