from collections import Counter
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        letters = [0] * 26
        universal = []
        offset = ord('a')
        for word in words2:
            for letter, count in Counter(word).items():
                letters[ord(letter) - offset] = max(letters[ord(letter) - offset], count)
        for word in words1:
            counter = Counter(word)
            if all(counter[chr(i + offset)] >= letters[i] for i in range(26)):
                universal.append(word)
        return universal


s = Solution()
print(s.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], words2=["e", "o"]))
