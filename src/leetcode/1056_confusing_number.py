class Solution:
    def confusingNumber(self, n: int) -> bool:
        confusing = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        before = n
        after = 0
        while n > 0:
            digit = n % 10
            if digit not in confusing.keys():
                return False
            after *= 10
            after += confusing[digit]
            n //= 10
        return before != after


s = Solution()
print(s.confusingNumber(6))
print(s.confusingNumber(89))
print(s.confusingNumber(11))
print(s.confusingNumber(0))
