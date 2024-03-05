import bisect


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def length_of_lis(self, nums):
        ans = [nums[0]]
        for num in nums[1:]:
            if num > ans[-1]:
                ans.append(num)
            else:
                idx = bisect.bisect_left(ans, num)
                ans[idx] = num
        return len(ans)


s = Solution()
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(s.lengthOfLIS([0, 1, 0, 3, 2, 3]))
print(s.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
print(s.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
