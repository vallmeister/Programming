class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        n = len(nums)
        ds_size = [1] * n
        prev_index = list(range(n))
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and ds_size[i] <= ds_size[j]:
                    ds_size[i] = ds_size[j] + 1
                    prev_index[i] = j
        max_size = max(ds_size)
        index = ds_size.index(max_size)
        ans = [nums[index]]
        while prev_index[index] != index:
            index = prev_index[index]
            ans.append(nums[index])
        return ans


s = Solution()
print(s.largestDivisibleSubset([1, 2, 3]))
print(s.largestDivisibleSubset([1, 2, 4, 8]))
print(s.largestDivisibleSubset([4, 8, 10, 240]))
print(s.largestDivisibleSubset([2, 4, 7, 8]))
