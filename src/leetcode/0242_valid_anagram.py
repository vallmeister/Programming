class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()
        n = len(s)
        if n != len(t):
            return False
        for i in range(n):
            if s[i] != t[i]:
                return False
        return True

    def is_anagram_counter(self, s, t):
        count = [0] * 26
        n = len(s)
        if n != len(t):
            return False
        for i in range(n):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        for num in count:
            if num != 0:
                return False
        return True


sol = Solution()
print(sol.isAnagram("anagram", t="nagaram"))
print(sol.isAnagram("rat", t="car"))
print(sol.is_anagram_counter("anagram", t="nagaram"))
print(sol.is_anagram_counter("rat", t="car"))
