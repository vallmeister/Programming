class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        values = {char: (value + 1) // 3 + 1 for value, char in enumerate('abcdefghijklmnopqrstuvwxyz')}
        n = len(word)
        ps = [0] * (n + 1)
        ans = 0
        for i in range(1, n + 1):
            ps[i] = ps[i - 1] + values[word[i - 1]]
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                if (ps[j] - ps[i - 1]) % (j - i + 1) == 0:
                    ans += 1
        return ans


s = Solution()
print(s.countDivisibleSubstrings('asdf'))
