class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_chars = [0] * 26
        for c in s:
            s_chars[ord(c) - ord('a')] += 1
        t_chars = [0] * 26
        for c in t:
            t_chars[ord(c) - ord('a')] += 1
        for i in range(26):
            if s_chars[i] != t_chars[i]:
                return chr(i + ord('a'))
        return ""

    # genius way
    def find_the_difference(self, s, t):
        total = 0
        for c in s + t:
            total ^= ord(c)
        return chr(total)


sol = Solution()
print(sol.findTheDifference("abcd", "abcde"))
print(sol.findTheDifference("", "y"))
print(sol.findTheDifference("a", "aa"))
