class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        fst = [-1] * 26
        lst = [-1] * 26
        for i, char in enumerate(s):
            alphabet = ord(char) - ord('a')
            if fst[alphabet] == -1:
                fst[alphabet] = i
            else:
                lst[alphabet] = i
        for i in range(26):
            palindromes = set()
            if fst[i] > -1 and lst[i] > -1:
                left = fst[i]
                right = lst[i]
                char = chr(i + ord('a'))
                for j in s[left + 1: right]:
                    palindromes.add(char + j + char)
            ans += len(palindromes)
        return ans


sol = Solution()
print(sol.countPalindromicSubsequence("aabca"))
print(sol.countPalindromicSubsequence("adc"))
print(sol.countPalindromicSubsequence("bbcbaba"))
