class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n in {1, 2}:
            return 1
        t0, t1, t2 = 0, 1, 1
        for i in range(3, n + 1):
            t2, t1, t0 = t2 + t1 + t0, t2, t1
        return t2


s = Solution()
print(s.tribonacci(4))
print(s.tribonacci(25))
