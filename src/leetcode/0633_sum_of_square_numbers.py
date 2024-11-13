class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 3:
            return True
        squares = set()
        a = 0
        while a * a <= c:
            squares.add(a * a)
            a += 1
        for square in squares:
            if c - square in squares:
                return True
        return False


s = Solution()
print(s.judgeSquareSum(5))
print(s.judgeSquareSum(3))
print(s.judgeSquareSum(100000000))
