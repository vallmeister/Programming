from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        n = len(words)
        for i in range(n):
            pattern = words[i]
            for j in range(n):
                if j == i:
                    continue
                word = words[j]
                if self.kmp(pattern, word):
                    ans.append(pattern)
                    break
        return ans

    def get_lps(self, p):
        m = len(p)
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if p[i] == p[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def kmp(self, pattern, s):
        m = len(pattern)
        n = len(s)
        lps = self.get_lps(pattern)
        i = j = 0
        while n - i >= m - j:
            if pattern[j] == s[i]:
                i += 1
                j += 1
            if j == m:
                return True
            elif i < n and pattern[j] != s[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return False
