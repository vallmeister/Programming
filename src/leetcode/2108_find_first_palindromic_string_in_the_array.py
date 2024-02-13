from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        def is_palindrome(s):
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        for word in words:
            if is_palindrome(word):
                return word
        return ""
