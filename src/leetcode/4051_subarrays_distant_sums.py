from sortedcontainers import sortedlist


class Solution:
    def distantSubarrays(self, nums: list[int], goal: int, k: int) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        if k == 0:
            return total
        prefix_sums = sortedlist.SortedList()
        prefix_sums.add(0)
        ps = 0
        ans = 0
        for i, num in enumerate(nums):
            ps += num
            j = prefix_sums.bisect_left(ps - goal + k)
            ans += i - j
            j = prefix_sums.bisect_right(ps - goal - k)
            ans += j + 1
            prefix_sums.add(ps)
        return ans


s = Solution()
print(s.distantSubarrays(nums=[1, 2, 1], goal=4, k=1))
print(s.distantSubarrays(nums=[2, -1, 3], goal=2, k=2))
print(s.distantSubarrays(nums=[-3, 1, 2], goal=0, k=3))
print(s.distantSubarrays([16, 26, 41, 20, -25, 18], -7, 0))
