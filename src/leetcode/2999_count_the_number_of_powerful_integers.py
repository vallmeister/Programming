class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        start_ = str(start - 1)
        finish_ = str(finish)
        return self.get_valid_numbers(finish_, s, limit) - self.get_valid_numbers(start_, s, limit)

    def get_valid_numbers(self, x, s, limit):
        if len(x) < len(s):
            return 0
        elif len(x) == len(s):
            return 1 if x >= s else 0

        pre_len = len(x) - len(s)
        suffix = x[pre_len:]
        count = 0

        for i in range(pre_len):
            if limit < int(x[i]):
                count += (limit + 1) ** (pre_len - i)
                return count
            count += int(x[i]) * (limit + 1) ** (pre_len - 1 - i)

        if suffix >= s:
            count += 1

        return count


sol = Solution()
print(sol.numberOfPowerfulInt(start=1, finish=6000, limit=4, s="124"))
print(sol.numberOfPowerfulInt(start=15, finish=215, limit=6, s="10"))
print(sol.numberOfPowerfulInt(start=1000, finish=2000, limit=4, s="3000"))
print(sol.numberOfPowerfulInt(start=20, finish=1159, limit=5, s='20'))  # expected 8
print(sol.numberOfPowerfulInt(15398, 1424153842, 8, '101'))
