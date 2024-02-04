from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        t_letters = Counter(t)
        ans = ''
        left = 0
        for right in range(m):
            curr_char = s[right]
            t_letters[curr_char] -= 1
            while all(v <= 0 for v in t_letters.values()):
                if not ans or len(ans) > right - left + 1:
                    ans = s[left:right + 1]
                curr_char = s[left]
                t_letters[curr_char] += 1
                left += 1
        return ans


sol = Solution()
print(sol.minWindow("ADOBECODEBANC", t="ABC"))
print(sol.minWindow("a", t="a"))
print(sol.minWindow(s="a", t="aa"))
print(sol.minWindow('ab', 'a'))
print(sol.minWindow("cabwefgewcwaefgcf", "cae"))
