class Solution:
    def mySqrt(self, x: int) -> int:
        lower = 0
        upper = x
        
        if x == 0:
            return 0
        elif x == 1:
            return 1

        while lower <= upper:
            mid = (lower + upper) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                upper = mid - 1
            else:
                if (mid + 1) * (mid + 1) <= x:
                    lower = mid + 1
                else:
                    return mid

s = Solution()
print(s.mySqrt(5))
print(s.mySqrt(8))
print(s.mySqrt(0))
