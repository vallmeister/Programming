from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        def get_bits(num):
            bits = 0
            while num > 0:
                if num % 2 == 1:
                    bits += 1
                num //= 2
            return bits

        return sorted(arr, key=lambda x: (get_bits(x), x))


s = Solution()
print(s.sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]))
print(s.sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))
