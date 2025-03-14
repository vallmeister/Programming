from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 1
        ans = 0
        right = max(candies)

        while left <= right:
            mid = (left + right) // 2
            if self.get_piles(candies, mid) >= k:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

    def get_piles(self, candies, num):
        return sum(c // num for c in candies)


s = Solution()
print(s.maximumCandies([5, 8, 6], 3))
print(s.maximumCandies([2, 5], 11))
print(s.maximumCandies([8, 7, 6], 4))
