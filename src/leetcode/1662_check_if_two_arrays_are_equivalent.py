from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        m = len(word1)
        n = len(word2)
        i_1, i_2 = 0, 0
        j_1, j_2 = 0, 0
        while i_1 < m and i_2 < n:
            if j_1 >= len(word1[i_1]) or j_2 >= len(word2[i_2]):
                if j_1 >= len(word1[i_1]):
                    j_1 = 0
                    i_1 += 1
                if j_2 >= len(word2[i_2]):
                    j_2 = 0
                    i_2 += 1
            elif word1[i_1][j_1] != word2[i_2][j_2]:
                return False
            else:
                j_1 += 1
                j_2 += 1
        if i_1 < m or i_2 < n:
            return False
        return True


s = Solution()
print(s.arrayStringsAreEqual(["ab", "c"], word2=["a", "bc"]))
print(s.arrayStringsAreEqual(["a", "cb"], word2=["ab", "c"]))
print(s.arrayStringsAreEqual(["abc", "d", "defg"], word2=["abcddefg"]))
