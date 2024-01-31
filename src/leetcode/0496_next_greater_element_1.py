from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        ms = []
        for num in nums2:
            while ms and ms[-1] < num:
                element = ms.pop()
                next_greater[element] = num
            ms.append(num)
        n = len(nums1)
        ans = [-1] * n
        for i, num in enumerate(nums1):
            if num in next_greater:
                ans[i] = next_greater[num]
        return ans


s = Solution()
print(s.nextGreaterElement([4, 1, 2], nums2=[1, 3, 4, 2]))
print(s.nextGreaterElement([2, 4], nums2=[1, 2, 3, 4]))
