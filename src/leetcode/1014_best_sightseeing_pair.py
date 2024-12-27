class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        n = len(values)
        val_j = [0] * n
        for j in range(n):
            val_j[j] = values[j] - j
        max_after = [0] * n
        max_after[-1] = -n
        for i in reversed(range(n - 1)):
            max_after[i] = max(max_after[i + 1], val_j[i + 1])
        ans = 0
        for i in range(n - 1):
            ans = max(ans, values[i] + i + max_after[i])
        return ans


s = Solution()
print(s.maxScoreSightseeingPair([8, 1, 5, 2, 6]))
print(s.maxScoreSightseeingPair([1, 2]))
print(s.maxScoreSightseeingPair([1, 1, 1]))
