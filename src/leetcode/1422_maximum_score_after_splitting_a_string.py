class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        score = 0
        zeroes = [0] * n
        ones = [0] * n
        for i in range(n):
            zeroes[i] = zeroes[i - 1] + 1 - int(s[i])
        for i in reversed(range(n - 1)):
            ones[i] = ones[i + 1] + int(s[i + 1])
        for i in range(n - 1):
            score = max(score, zeroes[i] + ones[i])
        return score


sol = Solution()
print(sol.maxScore("011101"))
print(sol.maxScore("00111"))
print(sol.maxScore("1111"))
