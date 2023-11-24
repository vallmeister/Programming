class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check_palindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return check_palindrome(left + 1, right) or check_palindrome(left, right - 1)
            left += 1
            right -= 1
        return True


sol = Solution()
print(sol.validPalindrome("aba"))
print(sol.validPalindrome("abca"))
print(sol.validPalindrome("abc"))
