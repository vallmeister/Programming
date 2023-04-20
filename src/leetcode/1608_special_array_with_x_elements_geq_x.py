class Solution:
    def specialArray(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(1, n + 1):
            for j in range(n):
                if nums[j] >= i:
                    if i == n - j:
                        return i
                    else:
                        break
        return -1


s = Solution()
print(s.specialArray([3, 5]))
print(s.specialArray([0, 0]))
print(s.specialArray([0, 4, 3, 0, 4]))
