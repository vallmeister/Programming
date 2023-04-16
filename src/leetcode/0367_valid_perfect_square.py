class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left = 2
        right = num // 2
        while left <= right:
            pivot = (left + right) // 2
            if pivot * pivot == num:
                return True
            elif pivot * pivot < num:
                left = pivot + 1
            elif pivot * pivot > num:
                right = pivot - 1
        return False


s = Solution()
print(s.isPerfectSquare(16))
print(s.isPerfectSquare(14))
