from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        for i in reversed(range(n)):
            if i + k < n:
                energy[i] += energy[i + k]
        return max(energy)


s = Solution()
print(s.maximumEnergy(energy=[5, 2, -10, -5, 1], k=3))
print(s.maximumEnergy(energy=[-2, -3, -1], k=2))
