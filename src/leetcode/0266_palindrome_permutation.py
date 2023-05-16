class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        chars = [0] * 26
        for c in s:
            chars[ord(c) - ord('a')] += 1
            chars[ord(c) - ord('a')] %= 2
        res = 0
        for num in chars:
            res += num
        return len(s) % 2 == 0 and res == 0 or len(s) % 2 == 1 and res == 1


sol = Solution()
print(sol.canPermutePalindrome('code'))
print(sol.canPermutePalindrome('aab'))
print(sol.canPermutePalindrome('carerac'))
print(sol.canPermutePalindrome('aaa'))
