class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        start = lower
        ans = []
        for num in nums:
            end = num - 1
            if start <= end:
                ans.append([start, end])
            start = num + 1
        if start <= upper:
            ans.append([start, upper])
        return ans


s = Solution()
print(s.findMissingRanges([0, 1, 3, 50, 75], 0, 99))
print(s.findMissingRanges([-1], -1, -1))
