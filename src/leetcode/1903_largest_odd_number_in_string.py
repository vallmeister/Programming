class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        ans = ''
        for i in reversed(range(n)):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ans


s = Solution()
print(s.largestOddNumber("52"))
print(s.largestOddNumber("4206"))
print(s.largestOddNumber("35427"))
