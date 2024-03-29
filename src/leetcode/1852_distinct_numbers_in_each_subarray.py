from typing import List


class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        window = {}
        for i in range(k - 1):
            num = nums[i]
            if num not in window:
                window[num] = 0
            window[num] += 1
        left = 0
        ans = []
        for right, num in enumerate(nums[k - 1:]):
            if num not in window:
                window[num] = 0
            window[num] += 1
            ans.append(len(window.keys()))
            left_num = nums[left]
            window[left_num] -= 1
            if window[left_num] == 0:
                del window[left_num]
            left += 1
        return ans


s = Solution()
print(s.distinctNumbers([1, 2, 3, 2, 2, 1, 3], k=3))
