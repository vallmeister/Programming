class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        ans = 0
        word2_count = [0] * 26
        for char in word2:
            word2_count[ord(char) - ord('a')] += 1
        left = 0
        n = len(word1)
        window = [0] * 26
        for r, char in enumerate(word1):
            window[ord(char) - ord('a')] += 1
            while all(window[i] >= word2_count[i] for i in range(26)):
                ans += n - r
                window[ord(word1[left]) - ord('a')] -= 1
                left += 1
        return ans
