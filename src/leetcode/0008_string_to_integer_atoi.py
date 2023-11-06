class Solution:
    def myAtoi(self, s: str) -> int:
        negative = False
        relevant = []
        i = 0
        n = len(s)

        # 1. Ignore leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check for sign
        if i < n and s[i] == '-':
            negative = True
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # 3. Read digits
        while i < n and s[i].isdigit():
            relevant.append(s[i])
            i += 1

        # 4. Convert digits to integer
        position = 1
        result = 0
        while relevant:
            result += int(relevant.pop()) * position
            position *= 10
        if negative:
            result *= -1

        # 5.Clamp integer
        if result < -2 ** 31:
            result = -2 ** 31
        elif result > 2 ** 31 - 1:
            result = 2 ** 31 - 1

        # 6. Return integer
        return result


sol = Solution()
print(sol.myAtoi('42'))
print(sol.myAtoi('   -42'))
print(sol.myAtoi('4193 with words'))
print(sol.myAtoi(" -1123u3761867"))  # -1123
print(sol.myAtoi("00000-42a1234"))  # 0
