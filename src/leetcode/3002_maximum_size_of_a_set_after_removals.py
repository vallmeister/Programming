
from typing import List


class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        set_1 = set(nums1)
        set_2 = set(nums2)
        final_set = set()
        left = set_1 - set_2
        while len(left) > n // 2:
            left.pop()
        final_set |= left
        right = set_2 - set_1
        while len(right) > n // 2:
            right.pop()
        final_set |= right
        count = len(left)
        for num in nums1:
            if count >= n // 2:
                break
            elif num in left or num in final_set:
                continue
            final_set.add(num)
            count += 1
        count = len(right)
        for num in nums2:
            if count >= n // 2:
                break
            elif num in right or num in final_set:
                continue
            final_set.add(num)
            count += 1

        return len(final_set)


s = Solution()
print(s.maximumSetSize([1, 2, 1, 2], nums2=[1, 1, 1, 1]))
print(s.maximumSetSize([1, 2, 3, 4, 5, 6], nums2=[2, 3, 2, 3, 2, 3]))
print(s.maximumSetSize([1, 1, 2, 2, 3, 3], nums2=[4, 4, 5, 5, 6, 6]))
