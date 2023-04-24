class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        distance = 0
        for idx, num1 in enumerate(nums1):
            left = idx
            right = len(nums2) - 1
            right_most_idx = idx
            while left <= right:
                mid = (left + right) // 2
                if nums2[mid] >= num1:
                    right_most_idx = max(right_most_idx, mid)
                    left = mid + 1
                else:
                    right = mid - 1
            distance = max(distance, right_most_idx - idx)
        return distance


s = Solution()
print(s.maxDistance([55, 30, 5, 4, 2], [100, 20, 10, 10, 5]))
print(s.maxDistance([2, 2, 2], [10, 10, 1]))
print(s.maxDistance([30, 29, 19, 5], [25, 25, 25, 25, 25]))
