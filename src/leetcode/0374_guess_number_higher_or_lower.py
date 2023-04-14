pick = 1


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    if num == pick:
        return 0
    elif num < pick:
        return 1
    elif num > pick:
        return -1


class Solution:
    def guessNumber(self, n: int) -> int:
        lower = 1
        while lower <= n:
            mid = (lower + n) // 2
            tmp = guess(mid)
            if tmp == 0:
                return mid
            elif tmp == -1:
                n = mid - 1
            elif tmp == 1:
                lower = mid + 1
        return 0


s = Solution()
print(s.guessNumber(3))
