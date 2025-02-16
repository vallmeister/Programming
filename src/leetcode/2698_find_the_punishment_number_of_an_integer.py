from math import ceil, log10


class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            if self.is_partitionable(i, i * i):
                ans += i * i
        return ans

    def is_partitionable(self, target, num):
        if target < 0:
            return False
        elif target == num == 0:
            return True
        elif num == 0:
            return False
        ans = False
        for i in range(1, ceil(log10(num)) + 2):
            power = 10 ** i
            ans = ans or self.is_partitionable(target - (num % power), num // power)
        return ans


s = Solution()
print(s.punishmentNumber(10))
print(s.punishmentNumber(37))
