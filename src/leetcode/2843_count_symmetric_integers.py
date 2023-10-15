class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        while low <= high:
            n = len(str(low))
            if n % 2 == 1:
                low += 1
                continue
            tmp = 0
            num = low
            for i in range(n // 2):
                tmp += num % 10
                num //= 10
            for i in range(n // 2):
                tmp -= num % 10
                num //= 10
            if tmp == 0:
                ans += 1
            low += 1
        return ans

s = Solution()
print(s.countSymmetricIntegers(1, 100))
print(s.countSymmetricIntegers(1200, 1230))
