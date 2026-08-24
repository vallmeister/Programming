from collections import defaultdict


class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        primes = self.get_prime_factors(max(nums))
        window = defaultdict(int)
        ans = left = 0
        for right, num in enumerate(nums):
            for p in primes[num]:
                window[p] += 1
            while len(window) > k:
                for p in primes[nums[left]]:
                    window[p] -= 1
                    if window[p] == 0:
                        del window[p]
                left += 1
            ans = max(ans, right - left + 1)
        return ans

    def get_prime_factors(self, n):
        factors = defaultdict(list)
        sieve = [True] * (n + 1)
        for i in range(2, n + 1):
            if not sieve[i]:
                continue
            factors[i].append(i)
            for j in range(i, n + 1, i):
                factors[j].append(i)
                sieve[j] = False
        return factors


s = Solution()
print(s.longestSubarray(nums=[7, 6, 10, 12, 11], k=3))
print(s.longestSubarray(nums=[4, 6, 9, 18], k=4))
print(s.longestSubarray(nums=[6, 10, 15], k=2))
