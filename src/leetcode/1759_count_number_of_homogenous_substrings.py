class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        ans = 0
        lst = s[0]
        i = 0
        while i < n:
            count = 0
            while i < n and s[i] == lst:
                count += 1
                i += 1
            if i < n:
                lst = s[i]
            ans += count * (count + 1) // 2
        return ans % MOD


sol = Solution()
print(sol.countHomogenous("abbcccaa"))
print(sol.countHomogenous('xy'))
print(sol.countHomogenous("zzzzz"))
