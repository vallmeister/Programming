from collections import Counter
from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)

        def backtracking(i):
            if i >= n:
                return 0
            elif not self.can_build_word(words[i], letters):
                return backtracking(i + 1)
            skip = backtracking(i + 1)
            for letter in words[i]:
                letters.remove(letter)
            build = sum(score[ord(letter) - ord('a')] for letter in words[i]) + backtracking(i + 1)
            for letter in words[i]:
                letters.append(letter)
            return max(skip, build)

        return backtracking(0)

    def can_build_word(self, word, letters):
        word_count = Counter(word)
        letter_count = Counter(letters)
        return all(letter_count[letter] >= count for letter, count in word_count.items())


s = Solution()
print(s.maxScoreWords(words=["dog", "cat", "dad", "good"], letters=["a", "a", "c", "d", "d", "d", "g", "o", "o"],
                      score=[1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
