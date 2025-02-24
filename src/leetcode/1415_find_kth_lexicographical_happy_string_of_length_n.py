class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        possibilities = 3 * 2 ** (n - 1)
        if k > possibilities:
            return ""
        happy = []
        third = possibilities // 3
        if k <= third:
            happy.append('a')
        elif k <= 2 * third:
            k -= third
            happy.append('b')
        else:
            k -= 2 * third
            happy.append('c')
        return self.recursive(n - 1, k, third, happy)

    def recursive(self, n, k, combinations, happy):
        if n == 0:
            return ''.join(happy)
        elif k > combinations:
            return ''
        half = combinations // 2
        prev = happy[-1]
        if k <= half:
            if prev == 'a':
                happy.append('b')
            else:
                happy.append('a')
        else:
            if prev == 'c':
                happy.append('b')
            else:
                happy.append('c')
            k -= half
        return self.recursive(n - 1, k, half, happy)


s = Solution()
print(s.getHappyString(1, 3))
print(s.getHappyString(1, 4))
print(s.getHappyString(3, 9))
