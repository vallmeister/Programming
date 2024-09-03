class Solution:
    def getLucky(self, s: str, k: int) -> int:
        char_to_num = {c: i + 1 for i, c in enumerate('abcdefghijklmnopqrstuvwxyz')}
        s = list(map(lambda c: str(char_to_num[c]), s))
        s = "".join(s)
        s = int(s)
        for _ in range(k):
            s = self.transform(s)
        return s

    def transform(self, num):
        s = 0
        while num > 0:
            s += num % 10
            num //= 10
        return s


sol = Solution()
print(sol.getLucky("iiii", k=1))
print(sol.getLucky("leetcode", k=2))
