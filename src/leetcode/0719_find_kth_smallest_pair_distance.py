import bisect
from collections import Counter
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = Counter(nums)
        leq = [0] * (nums[-1] + 1)
        for i in range(len(leq)):
            leq[i] = bisect.bisect_right(nums, i)

        left = 0
        right = max(nums) - min(nums)

        def num_pairs_smaller_than(x):
            ans = 0
            for num in nums:
                ans += leq[min(num + x, len(leq) - 1)]
                ans -= leq[num]
            ans += sum(v * (v - 1) // 2 for v in count.values())
            return ans

        res = 0
        while left <= right:
            mid = (left + right) // 2
            smaller_pairs = num_pairs_smaller_than(mid)
            if smaller_pairs >= k:
                right = mid - 1
                res = mid
            elif smaller_pairs < k:
                left = mid + 1

        return res


s = Solution()
print(s.smallestDistancePair([1, 3, 1], k=1))
print(s.smallestDistancePair([1, 1, 1], k=2))
print(s.smallestDistancePair([1, 6, 1], k=3))
print(s.smallestDistancePair([62, 100, 4], 2))
print(s.smallestDistancePair(
    [95, 29, 47, 58, 80, 65, 26, 7, 69, 0, 1, 53, 61, 46, 66, 30, 78, 25, 1, 62, 5, 1, 78, 60, 81, 100, 52, 33, 9, 52,
     7, 74, 94, 93, 47, 68, 80, 81, 50, 31, 9, 96, 8, 8, 64, 4, 40, 22, 50, 93], 1142))
