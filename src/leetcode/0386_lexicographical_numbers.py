from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        for i in range(10):
            self.dfs(n, i, ans)
        return ans

    def dfs(self, n, num, ans):
        if num < 1 or num > n:
            return
        ans.append(num)
        num *= 10
        for i in range(10):
            self.dfs(n, num + i, ans)
