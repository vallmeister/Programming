class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars = [0] * 26
        for char in s1:
            s1_chars[ord(char) - ord('a')] += 1
        window = [0] * 26
        left = 0
        for right, char in enumerate(s2):
            window[ord(char) - ord('a')] += 1
            while left < len(s2) and window[ord(s2[left]) - ord('a')] > s1_chars[ord(s2[left]) - ord('a')]:
                window[ord(s2[left]) - ord('a')] -= 1
                left += 1
            if all(window[i] == s1_chars[i] for i in range(26)):
                return True
        return False
