class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        digit_string = self.countAndSay(n - 1)
        m = len(digit_string)
        streak = 1
        prev = digit_string[0]
        ans = []
        for i in range(1, m + 1):
            if i == m:
                ans.append(str(streak))
                ans.append(str(prev))
                continue
            char = digit_string[i]
            if char == prev:
                streak += 1
            else:
                ans.append(str(streak))
                ans.append(str(prev))
                streak = 1
                prev = char
        return ''.join(ans)


s = Solution()
print(s.countAndSay(1))
print(s.countAndSay(2))
print(s.countAndSay(3))
print(s.countAndSay(4))
print(s.countAndSay(5))
