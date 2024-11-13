import bisect
from typing import List


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = self.generate_primes_until(max(nums))
        for i in reversed(range(len(nums) - 1)):
            if nums[i] < nums[i + 1]:
                continue
            diff = nums[i] - nums[i + 1] + 1
            j = bisect.bisect_left(primes, diff)
            if primes[j] >= nums[i]:
                return False
            nums[i] -= primes[j]
        return True

    def generate_primes_until(self, n):
        primes = [2]
        curr = 3
        while primes[-1] <= n:
            for p in primes:
                if curr % p == 0:
                    break
            else:
                primes.append(curr)
            curr += 2
        return primes


s = Solution()
print(s.primeSubOperation([5, 8, 3]))
