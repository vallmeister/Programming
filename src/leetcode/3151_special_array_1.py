from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        prev_parity = nums[0] & 1
        for num in nums[1:]:
            parity = num & 1
            if prev_parity == parity:
                return False
            prev_parity = parity
        return True
