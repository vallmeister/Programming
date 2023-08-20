class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        for i in range(len(s)):
            cs = s[i]
            ct = t[i]
            if cs in s_to_t and s_to_t[cs] != ct:
                return False
            if ct in t_to_s and t_to_s[ct] != cs:
                return False
            if cs not in s_to_t:
                s_to_t[cs] = ct
            if ct not in t_to_s:
                t_to_s[ct] = cs
        return True


sol = Solution()
print(sol.isIsomorphic('egg', 'add'))
print(sol.isIsomorphic('foo', 'bar'))
print(sol.isIsomorphic('paper', 'title'))
