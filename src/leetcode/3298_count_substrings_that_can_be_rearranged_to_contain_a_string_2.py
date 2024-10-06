class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        ans = 0
        window = [0] * 26
        for char in word2:
            window[ord(char) - ord('a')] -= 1
        n = len(word1)
        left = 0
        for r, char in enumerate(word1):
            window[ord(char) - ord('a')] += 1
            while min(window) >= 0:
                ans += n - r
                window[ord(word1[left]) - ord('a')] -= 1
                left += 1
        return ans
