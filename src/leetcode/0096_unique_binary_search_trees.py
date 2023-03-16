class Solution:
    memo = {0: 1, 1: 1}

    def numTrees(self, n: int) -> int:
        return self.num_trees_memo(n)

    def num_trees_memo(self, n):
        if n in self.memo:
            return self.memo[n]
        result = 0
        for i in range(1, n + 1):
            result += self.numTrees(i - 1) * self.numTrees(n - i)
        self.memo[n] = result
        return result


s = Solution()
print(s.numTrees(3))
print(s.numTrees(1))
print(s.numTrees(4))
print(s.numTrees(19))
