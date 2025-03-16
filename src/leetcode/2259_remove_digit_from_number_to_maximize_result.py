class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        number = list(number)
        ans = 0
        n = len(number)
        for i in range(n):
            if number[i] == digit:
                del number[i]
                ans = max(ans, int(''.join(number)))
                number.insert(i, digit)
        return str(ans)
