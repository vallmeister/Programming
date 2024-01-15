class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keys = [-1] * 26
        for idx, key in enumerate(keyboard):
            keys[ord(key) - ord('a')] = idx
        t = pos = 0
        for char in word:
            idx = keys[ord(char) - ord('a')]
            t += abs(idx - pos)
            pos = idx
        return t


s = Solution()
print(s.calculateTime(keyboard="abcdefghijklmnopqrstuvwxyz", word="cba"))
print(s.calculateTime(keyboard="pqrstuvwxyzabcdefghijklmno", word="leetcode"))
