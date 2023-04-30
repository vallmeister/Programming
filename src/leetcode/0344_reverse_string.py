class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]


sol = Solution()
word = ["h", "e", "l", "l", "o"]
sol.reverseString(word)
print(word)
word = ["H", "a", "n", "n", "a", "h"]
sol.reverseString(word)
print(word)
