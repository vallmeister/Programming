class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        count = [0] * 1001
        for num in nums:
            count[num] += 1
        for i in reversed(range(1001)):
            if count[i] == 1:
                return i
        return -1


s = Solution()
print(s.largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 1]))
print(s.largestUniqueNumber([9, 9, 8, 8]))
