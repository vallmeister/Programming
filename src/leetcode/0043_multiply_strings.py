class Solution:
    # TODO: revisit and implement more by hand
    def multiply(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)
        ans = 0
        for i in range(m):
            for j in range(n):
                digit_1 = int(num1[i])
                digit_2 = int(num2[j])
                ans += digit_1 * digit_2 * 10 ** (m - i - 1) * 10 ** (n - j - 1)
        return str(ans)


s = Solution()
print(s.multiply('2', '3'))
print(s.multiply('123', '456'))
