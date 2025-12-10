from collections import Counter
from typing import List


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        mn = min(complexity)
        freq = Counter(complexity)
        if complexity[0] != mn or freq[complexity[0]] > 1:
            return 0
        ans = 1
        MOD = 10 ** 9 + 7
        for i in range(1, len(complexity)):
            ans *= i
            ans %= MOD
        return ans
