from collections import defaultdict
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        products = defaultdict(list)
        nums.sort()
        for i in range(n):
            for j in range(i + 1, n):
                a = nums[i]
                b = nums[j]
                products[a * b].append([a, b])
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                a = nums[i]
                b = nums[j]
                p = products[a * b]
                ans += len(p) + 1
                cs, ds = zip(*p)
                cs = list(cs)
                cs.sort()
                ans -= (self.bin_search_right(cs, a) - self.bin_search_left(cs, a) + 1)
                ds = list(ds)
                ds.sort()
                ans -= (self.bin_search_right(ds, b) - self.bin_search_left(ds, b) + 1)
        return 4 * ans

    def bin_search_left(self, arr, target):
        n = len(arr)
        left = 0
        right = n - 1
        ans = n
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                ans = min(ans, mid)
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1
        return ans

    def bin_search_right(self, arr, target):
        n = len(arr)
        left = ans = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                ans = max(ans, mid)
                left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1
        return ans


s = Solution()
print(s.tupleSameProduct([2, 3, 4, 6]))
print(s.tupleSameProduct([1, 2, 4, 5, 10]))
