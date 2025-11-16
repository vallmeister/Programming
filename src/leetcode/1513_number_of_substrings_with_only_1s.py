class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        seq = 0
        MOD = 10 ** 9 + 7
        for c in s:
            if c == '0':
                seq = 0
            elif c == '1':
                seq += 1
                ans += seq
                ans %= MOD
        return ans


sol = Solution()
print(sol.numSub("0110111"))
print(sol.numSub('101'))
print(sol.numSub("111111"))
