
class Solution:
    def twoEggDrop(self, n: int) -> int:
        ans = 0
        count = 0
        while count < n:
            ans += 1
            count += ans
        return ans


print(Solution().twoEggDrop(2))
print(Solution().twoEggDrop(100))
