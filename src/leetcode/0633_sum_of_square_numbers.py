class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 3:
            return True
        a = 0
        while a * a <= c:
            b = c - a * a
            left = 0
            right = b
            while left <= right:
                mid = (left + right) // 2
                if mid * mid == b:
                    return True
                elif mid * mid < b:
                    left = mid + 1
                elif mid * mid > b:
                    right = mid - 1
            a += 1
        return False


s = Solution()
print(s.judgeSquareSum(5))
print(s.judgeSquareSum(3))
print(s.judgeSquareSum(100000000))
