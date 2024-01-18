class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = 0
        for i in range(31):
            if right - left >= 2 ** i:
                continue
            else:
                mask = 1 << i
                ans |= right & left & mask
        return ans


s = Solution()
print(s.rangeBitwiseAnd(5, 7))
print(s.rangeBitwiseAnd(0, 0))
print(s.rangeBitwiseAnd(1, 2147483647))
