from heapq import heappush, heappop


class Solution:
    def sortVowels(self, s: str) -> str:
        n = len(s)
        vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
        vowel_heap = []
        t = [''] * n
        for i in range(n):
            if s[i] in vowels:
                heappush(vowel_heap, s[i])
            else:
                t[i] = s[i]
        for i in range(n):
            if not t[i]:
                t[i] = heappop(vowel_heap)
        return ''.join(t)


sol = Solution()
print(sol.sortVowels("lEetcOde"))
print(sol.sortVowels("lYmpH"))