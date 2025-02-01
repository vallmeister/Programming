from typing import List


class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        frequencies = [0] * (10 ** 5 + 1)
        distinct = 0
        ans = []
        for i in range(k - 1):
            if frequencies[nums[i]] == 0:
                distinct += 1
            frequencies[nums[i]] += 1
        left = 0
        for right in range(k - 1, n):
            if frequencies[nums[right]] == 0:
                distinct += 1
            frequencies[nums[right]] += 1
            ans.append(distinct)

            left_num = nums[left]
            frequencies[left_num] -= 1
            if frequencies[left_num] == 0:
                distinct -= 1
            left += 1
        return ans


s = Solution()
print(s.distinctNumbers([1, 2, 3, 2, 2, 1, 3], k=3))
print(s.distinctNumbers([1, 1, 1, 1, 2, 3, 4], 4))
