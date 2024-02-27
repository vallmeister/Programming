from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        deletions = 0
        frequencies = sorted(Counter(s).values(), reverse=True)
        unique_frequencies = set()
        while frequencies:
            freq = frequencies.pop()
            while freq > 0 and freq in unique_frequencies:
                freq -= 1
                deletions += 1
            if freq > 0:
                unique_frequencies.add(freq)
        return deletions
