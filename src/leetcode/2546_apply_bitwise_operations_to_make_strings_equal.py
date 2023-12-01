class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        if s == target:
            return True
        zeroes_s = 0
        ones_s = 0
        zeroes_target = 0
        ones_target = 0
        n = len(s)
        for i in range(n):
            if s[i] == '0':
                zeroes_s += 1
            elif s[i] == '1':
                ones_s += 1
            if target[i] == '0':
                zeroes_target += 1
            elif target[i] == '1':
                ones_target += 1
        if ones_s > 0 and ones_target == 0:
            return False
        elif ones_s == 0 and ones_target > 0:
            return False
        return True


sol = Solution()
print(sol.makeStringsEqual("1010", target="0110"))
print(sol.makeStringsEqual("11", target="00"))
print(sol.makeStringsEqual('00', '10'))
