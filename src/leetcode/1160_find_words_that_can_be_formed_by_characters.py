from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_counter = Counter(chars)
        ans = 0
        for word in words:
            tmp = Counter(word)
            for char, cnt in tmp.items():
                if chars_counter[char] < cnt:
                    break
            else:
                ans += len(word)
        return ans


s = Solution()
print(s.countCharacters(["cat", "bt", "hat", "tree"], chars="atach"))
print(s.countCharacters(["hello", "world", "leetcode"], chars="welldonehoneyr"))
