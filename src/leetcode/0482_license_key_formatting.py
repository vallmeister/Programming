from collections import deque


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = deque()
        n = len(s)
        i = n - 1
        curr_group = 0

        while i >= 0:
            if curr_group == k:
                ans.appendleft('-')
                curr_group = 0
            elif s[i] == '-':
                i -= 1
            elif s[i].isalpha():
                ans.appendleft(s[i].upper())
                i -= 1
                curr_group += 1
            else:
                ans.appendleft(s[i])
                i -= 1
                curr_group += 1
        if ans and ans[0] == '-':
            ans.popleft()

        return ''.join(ans)


sol = Solution()
print(sol.licenseKeyFormatting("5F3Z-2e-9-w", k=4))
print(sol.licenseKeyFormatting("2-5g-3-J", k=2))
print(sol.licenseKeyFormatting("---", 3))
