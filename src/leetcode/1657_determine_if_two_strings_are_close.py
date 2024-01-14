from itertools import zip_longest
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter_1 = sorted(Counter(word1).values())
        counter_2 = sorted(Counter(word2).values())
        letters_1 = set(word1)
        letters_2 = set(word2)

        return all(c1 == c2 for c1, c2 in zip_longest(counter_1, counter_2)) and all(
            l2 in letters_1 for l2 in word2) and all(l1 in letters_2 for l1 in word1)


print(Solution().closeStrings("abc", word2="bca"))
print(Solution().closeStrings("a", word2="aa"))
print(Solution().closeStrings("cabbba", word2="abbccc"))
print(Solution().closeStrings('uau', 'ssx'))
