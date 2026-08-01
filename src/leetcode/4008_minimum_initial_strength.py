class Solution:
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
        n = len(monsters)
        total_boost = [0] * (n + 1)
        for l, r, v in boosts:
            total_boost[l] += v
            total_boost[r + 1] -= v
        lower = 0
        upper = ans = 5 * 10 ** 13
        while lower <= upper:
            mid = (lower + upper) // 2
            if self.validate(monsters, total_boost, mid):
                ans = mid
                upper = mid - 1
            else:
                lower = mid + 1
        return ans

    def validate(self, monsters, total_boost, strength):
        bonus = 0
        n = len(monsters)
        for i in range(n):
            bonus += total_boost[i]
            if monsters[i] > strength + bonus:
                return False
            strength = max(0, strength - monsters[i])
        return True


s = Solution()
print(s.minInitialStrength(monsters=[5, 10, 15], boosts=[[1, 1, 10]]))
print(s.minInitialStrength(monsters=[5, 10, 15], boosts=[[1, 2, 10], [1, 2, 5]]))
