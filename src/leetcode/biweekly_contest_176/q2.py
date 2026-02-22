from collections import defaultdict
from typing import List


class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        groups = defaultdict(int)
        for word in words:
            if len(word) < k:
                continue
            groups[word[:k]] += 1
        return sum(1 if size >= 2 else 0 for size in groups.values())
