class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        ones = 0
        for digit in s:
            if digit == '1':
                ones += 1
        zeros = 0
        score = 0
        for digit in s[:n - 1]:
            if digit == '1':
                ones -= 1
            elif digit == '0':
                zeros += 1
            score = max(score, zeros + ones)
        return score


sol = Solution()
print(sol.maxScore("011101"))
print(sol.maxScore("00111"))
print(sol.maxScore("1111"))
