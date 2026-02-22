from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        offset = ord('a')
        ans = []
        for word in words:
            weight = 0
            for c in word:
                weight += weights[ord(c) - offset]
                weight %= 26
            ans.append(chr(25 - weight + offset))
        return ''.join(ans)


s = Solution()
print(s.mapWordWeights(words=["abcd", "def", "xyz"],
                       weights=[5, 3, 12, 14, 1, 2, 3, 2, 10, 6, 6, 9, 7, 8, 7, 10, 8, 9, 6, 9, 9, 8, 3, 7, 7, 2]))
