from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        t_dict = Counter(t)
        left = 0
        right = 0
        ans = ""
        curr_window = defaultdict(int)
        curr_size = 0

        def check_window():
            for letter, occurrences in t_dict.items():
                if curr_window[letter] < occurrences:
                    return False
            return True

        while right < m:
            while right < m and not check_window():
                character = s[right]
                curr_window[character] += 1
                curr_size += 1
                right += 1
            while left <= right and check_window():
                if not ans or curr_size < len(ans):
                    ans = s[left:right]
                character = s[left]
                curr_window[character] -= 1
                curr_size -= 1
                left += 1
        return ans


sol = Solution()
print(sol.minWindow("ADOBECODEBANC", t="ABC"))
print(sol.minWindow("a", t="a"))
print(sol.minWindow(s="a", t="aa"))
print(sol.minWindow('ab', 'a'))
print(sol.minWindow("cabwefgewcwaefgcf", "cae"))
