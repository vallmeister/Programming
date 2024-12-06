class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m = len(str1)
        n = len(str2)
        i = j = 0
        while i < m:
            if j < n and (ord(str2[j]) - ord(str1[i]) + 26) % 26 <= 1:
                j += 1
            i += 1
        return j == n
