class Solution:
    def reverseWords(self, s: str) -> str:
        ans = list(s)
        idx = 0
        n = len(s)
        while idx < n:
            start = idx
            end = idx + 1
            while end < n and ans[end] != ' ':
                end += 1
            idx = end + 1
            end -= 1
            while start < end:
                ans[start], ans[end] = ans[end], ans[start]
                start += 1
                end -= 1
        return ''.join(ans)

    def reverse_words_cheat(self, s):
        return ' '.join(i[::-1] for i in s.split())


sol = Solution()
print(sol.reverseWords("Let's take LeetCode contest"))
print(sol.reverseWords("God Ding"))
print(sol.reverse_words_cheat("Let's take LeetCode contest"))
print(sol.reverse_words_cheat("God Ding"))
