class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        ans = mask = 0
        char_map = [0] * 26
        char_map[ord('a') - ord('a')] = 1
        char_map[ord('e') - ord('a')] = 2
        char_map[ord('i') - ord('a')] = 4
        char_map[ord('o') - ord('a')] = 8
        char_map[ord('u') - ord('a')] = 16
        memo = [-1] * 32
        for i in range(len(s)):
            mask ^= char_map[ord(s[i]) - ord('a')]
            if memo[mask] == -1 and mask != 0:
                memo[mask] = i
            ans = max(ans, i - memo[mask])
        return ans
