from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        prev = words[0]
        prev_chars = ''.join(sorted(prev))
        for word in words[1:]:
            curr_chars = ''.join(sorted(word))
            if prev_chars == curr_chars:
                continue
            ans.append(prev)
            prev = word
            prev_chars = curr_chars
        ans.append(prev)
        return ans


s = Solution()
print(s.removeAnagrams(words=["abba", "baba", "bbaa", "cd", "cd"]))
print(s.removeAnagrams(words=["a", "b", "c", "d", "e"]))
