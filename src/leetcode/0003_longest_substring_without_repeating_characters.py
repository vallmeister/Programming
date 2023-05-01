class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = [0] * 128
        i = 0
        j = 0
        max_so_far = 0
        while j < len(s):
            if letters[ord(s[j])] == 0:
                letters[ord(s[j])] += 1
                j += 1
            elif letters[ord(s[j])] > 0:
                letters[ord(s[i])] -= 1
                i += 1
            max_so_far = max(max_so_far, j - i)
        return max_so_far


sol = Solution()
print(sol.lengthOfLongestSubstring('abcabcbb'))
print(sol.lengthOfLongestSubstring('bbbbb'))
print(sol.lengthOfLongestSubstring('pwwkew'))
print(sol.lengthOfLongestSubstring(' '))
