from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        powers = []
        p = 0
        while n > 0:
            if n % 2:
                powers.append(p)
            n //= 2
            p += 1
        m = len(powers)
        ps = [0] * (m + 1)
        for i in range(m):
            ps[i + 1] = ps[i] + powers[i]

        ans = []
        for start, end in queries:
            power = ps[end + 1] - ps[start]
            ans.append(self.mod_exp(2, power, MOD))
        return ans

    def mod_exp(self, base, exp, mod):
        ans = 1
        while exp > 0:
            if exp % 2:
                ans *= base
                ans %= mod
                exp -= 1
            else:
                base *= base
                base %= mod
                exp //= 2
        return ans


s = Solution()
print(s.productQueries(n=15, queries=[[0, 1], [2, 2], [0, 3]]))
print(s.productQueries(n=2, queries=[[0, 0]]))
print(s.productQueries(n=13, queries=[[1, 2], [1, 1]]))
