class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        substrings = {}
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n + 1):
                ss = s[i:j]
                if ss not in substrings:
                    substrings[ss] = 0
                substrings[ss] += 1
        return max([0] + [len(substring) for substring in substrings if substrings[substring] >= 2])
