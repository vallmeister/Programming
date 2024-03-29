class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        ans = 0
        chars = set()
        left = 0
        for right, letter in enumerate(s):
            while letter in chars:
                left_char = s[left]
                chars.remove(left_char)
                left += 1
            chars.add(letter)
            ans += right - left + 1
        return ans
