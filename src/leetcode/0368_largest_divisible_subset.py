class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        n = len(nums)
        ans = []
        eds = [[] for _ in range(n)]
        for i in range(n):
            for j in reversed(range(i)):
                if nums[i] % nums[j] == 0 and len(eds[j]) > len(eds[i]):
                    eds[i] = list(eds[j])
            eds[i].append(nums[i])

        for subset in eds:
            if len(subset) > len(ans):
                ans = subset
        return ans


s = Solution()
print(s.largestDivisibleSubset([1, 2, 3]))
print(s.largestDivisibleSubset([1, 2, 4, 8]))
print(s.largestDivisibleSubset([4, 8, 10, 240]))
print(s.largestDivisibleSubset([2, 4, 7, 8]))
