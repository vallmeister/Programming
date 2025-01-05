from typing import List


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                subarray = nums[i:j]
                if self.prod(subarray) == self.lcm_arr(subarray) * self.gcd_arr(subarray):
                    ans = max(ans, j - i)
        return ans

    def gcd(self, a, b):
        if a < b:
            return self.gcd(b, a)
        elif b == 0:
            return a
        return self.gcd(b, a % b)

    def lcm(self, a, b):
        return a * b // self.gcd(a, b)

    def prod(self, arr):
        prod = 1
        for num in arr:
            prod *= num
        return prod

    def gcd_arr(self, arr):
        gcd = arr[0]
        for num in arr[1:]:
            gcd = self.gcd(gcd, num)
        return gcd

    def lcm_arr(self, arr):
        lcm = arr[0]
        for num in arr[1:]:
            lcm = self.lcm(lcm, num)
        return lcm


s = Solution()
print(s.maxLength([1, 2, 1, 2, 1, 1, 1]))
print(s.maxLength([2, 3, 4, 5, 6]))
