import bisect


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        indices = [[] for _ in range(26)]
        offset = ord('a')
        for i, c in enumerate(s):
            indices[ord(c) - offset].append(i)

        for i in range(26):
            outer_chars = indices[i]
            if len(outer_chars) < 2:
                continue
            left = outer_chars[0]
            right = outer_chars[-1]
            for j in range(26):
                inner_char = indices[j]
                if not inner_char:
                    continue
                k = bisect.bisect_right(inner_char, left)
                if k < len(inner_char) and left < inner_char[k] < right:
                    ans += 1
        return ans


sol = Solution()
print(sol.countPalindromicSubsequence("aabca"))
print(sol.countPalindromicSubsequence("adc"))
print(sol.countPalindromicSubsequence("bbcbaba"))
