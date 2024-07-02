from collections import defaultdict


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersection = []
        count = defaultdict(int)
        for num in nums1:
            count[num] += 1
        for num in nums2:
            if count[num] > 0:
                intersection.append(num)
                count[num] -= 1
        return intersection


s = Solution()
print(s.intersect([1, 2, 2, 1], [2, 2]))
print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
