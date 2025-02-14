from collections import Counter


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        mismatches = 0
        for i in range(n):
            if s1[i] != s2[i]:
                mismatches += 1

        c1 = Counter(s1)
        c2 = Counter(s2)

        return mismatches in {0, 2} and all(c1[chr(i + ord('a'))] == c2[chr(i + ord('a'))] for i in range(26))
