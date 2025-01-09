from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        pairs = 0
        n = len(words)
        for i in range(n):
            w1 = words[i]
            for j in range(i + 1, n):
                w2 = words[j]
                if w2.startswith(w1) and w2.endswith(w1):
                    pairs += 1
        return pairs
