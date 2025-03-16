from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq = Counter(s)
        return sum(f % 2 for f in freq.values()) == len(s) % 2


sol = Solution()
print(sol.canPermutePalindrome('code'))
print(sol.canPermutePalindrome('aab'))
print(sol.canPermutePalindrome('carerac'))
print(sol.canPermutePalindrome('aaa'))
