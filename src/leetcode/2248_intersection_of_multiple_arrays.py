from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        curr_max = 0
        for arr in nums:
            arr.sort()
            curr_max = max(curr_max, arr[0])
        indices = [0] * n
        bounded = [True] * n
        ans = []
        while all(bounded):
            for i in range(n):
                while indices[i] < len(nums[i]) and nums[i][indices[i]] < curr_max:
                    indices[i] += 1
                bounded[i] = indices[i] < len(nums[i])
                if not bounded[i]:
                    break
                elif nums[i][indices[i]] > curr_max:
                    curr_max = nums[i][indices[i]]
                    break
            else:
                ans.append(curr_max)
                for i in range(n):
                    indices[i] += 1
                    bounded[i] = indices[i] < len(nums[i])
        return ans


s = Solution()
print(s.intersection([[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]))
print(s.intersection([[1, 2, 3], [4, 5, 6]]))
