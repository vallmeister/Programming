class Solution:
    # TODO: revise
    def calculate(self, s: str) -> int:
        n = len(s)

        def eval(i):
            tmp = 0
            sign = 1
            while i < n:
                if s[i].isdigit():
                    start = i
                    while i < n and s[i].isdigit():
                        i += 1
                    tmp += sign * int(s[start:i])
                    i -= 1
                    sign = 1
                elif s[i] == '-':
                    sign = -1
                elif s[i] == '(':
                    par, i = eval(i + 1)
                    tmp += sign * par
                    sign = 1
                elif s[i] == ')':
                    return tmp, i
                i += 1
            return tmp, i

        return eval(0)[0]


sol = Solution()
print(sol.calculate("1 + 1"))
print(sol.calculate(" 2-1 + 2 "))
print(sol.calculate("(1+(4+5+2)-3)+(6+8)"))
print(sol.calculate("2147483647"))
