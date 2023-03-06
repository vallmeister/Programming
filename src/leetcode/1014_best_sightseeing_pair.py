class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        curr = 0
        result = 0
        for val in values:
            result = max(result, curr + val)
            curr = max(curr, val) - 1
        return result


s = Solution()
print(s.maxScoreSightseeingPair([8, 1, 5, 2, 6]))
print(s.maxScoreSightseeingPair([1, 2]))
