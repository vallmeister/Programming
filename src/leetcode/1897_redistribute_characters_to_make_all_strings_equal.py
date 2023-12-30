from collections import Counter
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        words = ''.join(words)
        counter = Counter(words)
        for _, count in counter.items():
            if count % n != 0:
                return False
        return True


s = Solution()
print(s.makeEqual(["abc", "aabc", "bc"]))
print(s.makeEqual(["ab", "a"]))
