class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        m, n = len(word1), len(word2)
        ans = []
        while i < m or j < n:
            if i < m:
                ans.append(word1[i])
                i += 1
            if j < n:
                ans.append(word2[j])
                j += 1
        return "".join(ans)


s = Solution()
print(s.mergeAlternately("abc", word2="pqr"))
print(s.mergeAlternately("ab", word2="pqrs"))
print(s.mergeAlternately("abcd", word2="pq"))
