class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        ans = '9' * (n + 1)
        used = [False] * 10
        num = []

        def backtrack(j):
            nonlocal ans
            if j >= n:
                ans = min(ans, ''.join([str(digit) for digit in num]))
                return
            elif pattern[j] == 'I' and num[-1] == 9 or pattern[j] == 'D' and num[-1] == 1:
                return
            elif ans[j] < str(num[j]):
                return
            if pattern[j] == 'I':
                for k in range(num[-1] + 1, 10):
                    if used[k]:
                        continue
                    used[k] = True
                    num.append(k)
                    backtrack(j + 1)
                    num.pop()
                    used[k] = False
            elif pattern[j] == 'D':
                for k in range(1, num[-1]):
                    if used[k]:
                        continue
                    used[k] = True
                    num.append(k)
                    backtrack(j + 1)
                    num.pop()
                    used[k] = False

        for i in range(1, 10):
            num.append(i)
            used[i] = True
            backtrack(0)
            num.pop()
            used[i] = False

        return ans


s = Solution()
print(s.smallestNumber("IIIDIDDD"))
print(s.smallestNumber("DDD"))
