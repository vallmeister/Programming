class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 2

        if n == 1:
            return first
        elif n == 2:
            return second
        else:
            for i in range(2, n):
                temp = second
                second = first + second
                first = temp
        return second

s = Solution()
print(s.climbStairs(2))    
print(s.climbStairs(3))    
print(s.climbStairs(38))