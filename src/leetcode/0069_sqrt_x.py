class Solution:
    def mySqrt(self, x: int) -> int:
        lower = 0
        upper = x
        while lower <= upper:
            mid = (lower + upper) // 2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            elif mid ** 2 > x:
                upper = mid - 1
            elif mid ** 2 < x:
                lower = mid + 1
        return -1


s = Solution()
print(s.mySqrt(4))
print(s.mySqrt(8))
