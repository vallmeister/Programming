from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()
        n = len(nums)
        for a in range(n):
            for b in range(a + 1, n):
                c = b + 1
                d = n - 1
                while c < d:
                    quadruple = (nums[a], nums[b], nums[c], nums[d])
                    if sum(quadruple) == target:
                        ans.add(quadruple)
                        c += 1
                    elif sum(quadruple) < target:
                        c += 1
                    elif sum(quadruple) > target:
                        d -= 1
        return [list(q) for q in ans]


s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], target=0))
print(s.fourSum([2, 2, 2, 2, 2], target=8))
