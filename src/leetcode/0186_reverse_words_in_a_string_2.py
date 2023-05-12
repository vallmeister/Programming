class Solution:
    def reverseWords(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        start = end = 0
        while end < len(s):
            while end < len(s) and s[end] != ' ':
                end += 1
            i, j = start, end - 1
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            start = end = end + 1


sol = Solution()
l1 = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
sol.reverseWords(l1)
print(l1)
l1 = ['a']
sol.reverseWords(l1)
print(l1)
