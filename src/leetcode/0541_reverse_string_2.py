class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ''
        while s:
            if len(s) < k:
                ans += s[::-1]
                return ans
            elif k <= len(s) < 2 * k:
                rev = s[:k]
                ans += rev[::-1] + s[k:]
                return ans
            else:
                rev = s[:k]
                ans += rev[::-1]
                s = s[k:]
                ans += s[:k]
                s = s[k:]
        return ans


sol = Solution()
print(sol.reverseStr('abcdefg', 2))
print(sol.reverseStr('abcd', 2))
