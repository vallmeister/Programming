class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        ans = ''
        for i in range(n - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                ans = max(ans, num[i])
        return 3 * ans


s = Solution()
print(s.largestGoodInteger("6777133339"))
print(s.largestGoodInteger("2300019"))
print(s.largestGoodInteger("42352338"))
