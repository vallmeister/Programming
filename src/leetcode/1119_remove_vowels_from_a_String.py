class Solution:
    def removeVowels(self, s: str) -> str:
        ans = []
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for c in s:
            if c in vowels:
                continue
            ans.append(c)
        return ''.join(ans)
