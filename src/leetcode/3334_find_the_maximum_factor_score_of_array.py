from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0] ** 2
        curr_gcd = curr_lcm = nums[0]
        for num in nums[1:]:
            curr_gcd = self.gcd(curr_gcd, num)
            curr_lcm = self.lcm(curr_lcm, num)
        ans = curr_lcm * curr_gcd

        curr_gcd = curr_lcm = nums[1]
        for num in nums[2:]:
            curr_gcd = self.gcd(curr_gcd, num)
            curr_lcm = self.lcm(curr_lcm, num)
        ans = max(ans, curr_lcm * curr_gcd)

        for skip in range(1, n):
            curr_gcd = curr_lcm = nums[0]
            for i in range(1, n):
                if i == skip:
                    continue
                curr_gcd = self.gcd(curr_gcd, nums[i])
                curr_lcm = self.lcm(curr_lcm, nums[i])
            ans = max(ans, curr_lcm * curr_gcd)
        return ans

    def gcd(self, a, b):
        while a > 0 and b > 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        if a == 0:
            return b
        return a

    def lcm(self, a, b):
        return a * b // self.gcd(a, b)


s = Solution()
print(s.lcm(s.lcm(14, 20), 6))
