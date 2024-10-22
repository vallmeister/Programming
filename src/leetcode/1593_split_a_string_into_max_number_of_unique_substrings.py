class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)

        def backtracking(start, words):
            if start >= n:
                return len(words)
            ans = 0
            for end in range(start + 1, n + 1):
                substring = s[start:end]
                if substring not in words:
                    words.add(substring)
                    ans = max(ans, backtracking(end, words))
                    words.remove(substring)
            return ans

        return backtracking(0, set())


sol = Solution()
print(sol.maxUniqueSplit('aba'))
print(sol.maxUniqueSplit('aa'))
