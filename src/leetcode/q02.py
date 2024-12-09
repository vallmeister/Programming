from typing import List


class Solution:
    def findMinimumTime(self, strength: List[int], K: int) -> int:
        strength.sort(reverse=True)
        return self.get_time(K, strength)

    def get_time(self, K, strength):
        time = 0
        energy = 0
        factor = 1
        while strength:
            time += 1
            energy += factor
            for i, num in enumerate(strength):
                if num <= energy:
                    del strength[i]
                    energy = 0
                    factor += K
        return time


s = Solution()
print(s.findMinimumTime([3, 4, 1], 1))
print(s.findMinimumTime([7, 3, 6, 18, 22, 50], 4))
