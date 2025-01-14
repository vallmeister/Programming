class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        letters = [0] * 26
        offset = ord('a')
        for letter in s:
            letters[ord(letter) - offset] += 1
        odd_letters = sum(letter % 2 for letter in letters)
        return n >= k >= odd_letters


sol = Solution()
print(sol.canConstruct("annabelle", k=2))
print(sol.canConstruct("leetcode", k=3))
print(sol.canConstruct("true", k=4))
