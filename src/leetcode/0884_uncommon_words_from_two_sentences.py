from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count_1 = Counter(s1.split())
        count_2 = Counter(s2.split())
        ans = []
        for word, count in count_1.items():
            if count == 1 and count_2[word] == 0:
                ans.append(word)
        for word, count in count_2.items():
            if count == 1 and count_1[word] == 0:
                ans.append(word)
        return ans
