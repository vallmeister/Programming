class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        for _ in range(1, n):
            prev = ans[0]
            count = 1
            new_ans = []
            for letter in ans[1:]:
                if letter == prev:
                    count += 1
                else:
                    new_ans.append(str(count) + prev)
                    prev = letter
                    count = 1
            new_ans.append(str(count) + prev)
            ans = ''.join(new_ans)
        return ans


s = Solution()
print(s.countAndSay(1))
print(s.countAndSay(2))
print(s.countAndSay(3))
print(s.countAndSay(4))
print(s.countAndSay(5))
print(s.countAndSay(6))
print(s.countAndSay(7))
