class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans = 0
        for i in range(k):
            if s[i] in vowels:
                ans += 1
        i = 0
        curr = ans
        while k < len(s):
            if s[k] in vowels:
                curr += 1
            if s[i] in vowels:
                curr -= 1
            ans = max(ans, curr)
            i += 1
            k += 1
        return ans


sol = Solution()
print(sol.maxVowels('abciiidef', 3))
print(sol.maxVowels('aeiou', 2))
print(sol.maxVowels('leetcode', 3))
