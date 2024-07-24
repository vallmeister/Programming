from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        def transform(number):
            if number == 0:
                return mapping[number]
            digits = []
            while number > 0:
                digits.append(number % 10)
                number //= 10
            for power, digit in enumerate(digits):
                number += mapping[digit] * 10 ** power
            return number

        return sorted(nums, key=lambda x: transform(x))
