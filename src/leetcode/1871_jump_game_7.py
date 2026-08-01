class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True
        left = -maxJump
        right = -minJump
        window = 0
        for i in range(1, n):
            if left >= 0 and dp[left]:
                window -= 1
            left += 1
            right += 1
            if right >= 0 and dp[right]:
                window += 1

            if s[i] == '1':
                continue
            dp[i] = window > 0

        return dp[-1]


sol = Solution()
print(sol.canReach(s="011010", minJump=2, maxJump=3))
print(sol.canReach(s="01101110", minJump=2, maxJump=3))
print(sol.canReach("0000000000", 2, 5))
print(sol.canReach("00111010", 3, 5))
