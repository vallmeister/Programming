class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        s_count = t_count = 0
        while i >= 0 or j >= 0:
            if i >= 0 and s[i] == '#' or j >= 0 and t[j] == '#':
                if i >= 0 and s[i] == '#':
                    s_count += 1
                    i -= 1
                if j >= 0 and t[j] == '#':
                    t_count += 1
                    j -= 1
            elif s_count > 0 or t_count > 0:
                if s_count > 0:
                    i -= 1
                    s_count -= 1
                if t_count > 0:
                    j -= 1
                    t_count -= 1
            elif i >= 0 and j >= 0 and s[i] == t[j]:
                i -= 1
                j -= 1
            else:
                return False
        return True


sol = Solution()
print(sol.backspaceCompare("ab#c", t="ad#c"))
print(sol.backspaceCompare("ab##", t="c#d#"))
print(sol.backspaceCompare("a#c", t="b"))
print(sol.backspaceCompare('a##c', '#a#c'))
print(sol.backspaceCompare("xywrrmp", "xywrrmu#p"))
print(sol.backspaceCompare("hd#dp#czsp#####", "hd#dp#czsp######"))
