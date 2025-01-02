from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        ps = [0] * (n + 1)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(n):
            ps[i] = ps[i - 1]
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                ps[i] += 1
        ans = []
        for l, r in queries:
            ans.append(ps[r] - ps[l - 1])
        return ans
