import math
from typing import List


class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [0] * n
        next_index = [-1] * n
        mx_val = mx_index = 0
        for i in reversed(range(n)):
            for j in range(i + 1, n):
                if groups[i] == groups[j] or self.get_hamming_distance(words[i], words[j]) != 1:
                    continue
                elif dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    next_index[i] = j
                if dp[i] > mx_val:
                    mx_val = dp[i]
                    mx_index = i

        return self.get_word_sequence(words, mx_index, next_index)

    def get_word_sequence(self, words, start, next_index):
        ans = []
        while start != -1:
            ans.append(words[start])
            start = next_index[start]
        return ans

    def get_hamming_distance(self, s1, s2):
        n = len(s1)
        if n != len(s2):
            return math.inf
        return sum(1 if s1[i] != s2[i] else 0 for i in range(n))


s = Solution()
print(s.getWordsInLongestSubsequence(words=["bab", "dab", "cab"], groups=[1, 2, 2]))
print(s.getWordsInLongestSubsequence(words=["a", "b", "c", "d"], groups=[1, 2, 3, 4]))
