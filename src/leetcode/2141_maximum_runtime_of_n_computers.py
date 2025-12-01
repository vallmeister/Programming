from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        lower = ans = 1
        upper = sum(batteries) // n
        while lower <= upper:
            mid = (lower + upper) // 2
            if self.is_valid(n, batteries, mid):
                ans = mid
                lower = mid + 1
            else:
                upper = mid - 1
        return ans

    def is_valid(self, n, batteries, time):
        energy = 0
        for power in batteries:
            energy += min(power, time)
        return energy // n >= time


s = Solution()
print(s.maxRunTime(n=2, batteries=[3, 3, 3]))
print(s.maxRunTime(n=2, batteries=[1, 1, 1, 1]))
