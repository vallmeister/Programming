import math
from collections import Counter
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        return sum((k + 1) * math.ceil(v / (k + 1)) for k, v in Counter(answers).items())


s = Solution()
print(s.numRabbits([1, 1, 2]))
print(s.numRabbits([10, 10, 10] * 4))
