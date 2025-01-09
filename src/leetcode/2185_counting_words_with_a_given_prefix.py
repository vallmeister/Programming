from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # alternatively, use Trie
        count = 0
        m = len(pref)
        for word in words:
            if len(word) < m:
                continue
            for i in range(m):
                if word[i] != pref[i]:
                    break
            else:
                count += 1
        return count
