class Solution:
    def findMin(self, nums: list[int]) -> int:
        ans = 5000

        def binary_search(start, end):
            if start > end:
                return
            mid = (start + end) // 2
            nonlocal ans
            if nums[start] <= nums[mid] <= nums[end]:
                ans = min(ans, nums[start])
                binary_search(0, start - 1)
            elif nums[start] <= nums[mid] >= nums[end]:
                ans = min(ans, nums[end], nums[start])
                binary_search(mid + 1, end)
            elif nums[start] >= nums[mid] <= nums[end]:
                ans = min(ans, nums[mid])
                binary_search(start + 1, mid - 1)
                binary_search(mid + 1, end - 1)

        binary_search(0, len(nums) - 1)
        return ans


s = Solution()
print(s.findMin([3, 4, 5, 1, 2]))
print(s.findMin([4, 5, 6, 7, 0, 1, 2]))
print(s.findMin([11, 13, 15, 17]))
