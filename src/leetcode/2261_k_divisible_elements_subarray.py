from typing import List


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        sub_arrays = set()
        for i in range(n):
            window = 0
            for j in range(i, n):
                if nums[j] % p == 0:
                    window += 1
                if window <= k:
                    sub_arrays.add(tuple(nums[i:j + 1]))
                else:
                    break

        return len(sub_arrays)
