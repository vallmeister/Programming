from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.sparse_values = {}
        for idx, num in enumerate(nums):
            if num != 0:
                self.sparse_values[idx] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for idx, num in self.sparse_values.items():
            if idx in vec.sparse_values:
                ans += num * vec.sparse_values[idx]
        return ans


nums1 = [1, 0, 0, 2, 3]
nums2 = [0, 3, 0, 4, 0]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
print(v1.dotProduct(v2))

nums1 = [0, 1, 0, 0, 0]
nums2 = [0, 0, 0, 0, 2]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
print(v1.dotProduct(v2))

nums1 = [0, 1, 0, 0, 2, 0, 0]
nums2 = [1, 0, 0, 0, 3, 0, 4]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
print(v1.dotProduct(v2))
