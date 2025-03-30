from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        primes = self.sieve_of_eratosthenes(max(nums))
        scores = self.get_prime_scores(nums, primes)

        next_greater_score = [n] * n
        mono_stack = []
        for i in range(n):
            while mono_stack and scores[mono_stack[-1]] < scores[i]:
                next_greater_score[mono_stack.pop()] = i
            mono_stack.append(i)

        prev_greater_score = [-1] * n
        mono_stack = []
        for i in reversed(range(n)):
            while mono_stack and scores[mono_stack[-1]] <= scores[i]:
                prev_greater_score[mono_stack.pop()] = i
            mono_stack.append(i)

        ans = 1
        for i, num in sorted(enumerate(nums), key=lambda x: -x[1]):
            ranges = (i - prev_greater_score[i]) * (next_greater_score[i] - i)
            impact = min(ranges, k)
            ans *= self.fast_exponentiation(num, impact, MOD)
            ans %= MOD
            k -= impact
            if k == 0:
                break
        return ans

    # too slow, use division for unique factors
    def get_prime_scores(self, nums, primes):
        scores = {}
        for num in nums:
            if num in scores:
                continue
            score = 0
            for p in primes:
                if num % p == 0:
                    score += 1
                elif p > num:
                    break
            scores[num] = score
        return [scores[num] for num in nums]

    def sieve_of_eratosthenes(self, upper):
        primes = []
        sieve = [True] * (upper + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, upper + 1):
            if not sieve[i]:
                continue
            primes.append(i)
            for j in range(i * i, upper + 1, i):
                sieve[j] = False
        return primes

    def fast_exponentiation(self, base, exp, mod):
        res = 1
        while exp > 0:
            if exp % 2 == 1:
                res *= base
                res %= mod

            base *= base
            base %= mod
            exp //= 2
        return res


s = Solution()
print(s.maximumScore([8, 3, 9, 3, 8], 2))
print(s.maximumScore([19, 12, 14, 6, 10, 18], 3))
