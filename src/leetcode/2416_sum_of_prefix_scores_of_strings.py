from typing import List


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = {}
        for word in words:
            curr = trie
            for letter in word:
                if letter not in curr:
                    curr[letter] = {}
                curr = curr[letter]
                if '*' not in curr:
                    curr['*'] = 0
                curr['*'] += 1
        ans = []
        for word in words:
            curr = trie
            score = 0
            for letter in word:
                curr = curr[letter]
                score += curr['*']
            ans.append(score)
        return ans
