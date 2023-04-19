class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        number = 1
        idx = 0
        misses = 0
        while misses < k:
            if idx >= len(arr):
                misses += 1
            elif arr[idx] == number:
                idx += 1
            else:
                misses += 1
            number += 1
        return number - 1


s = Solution()
print(s.findKthPositive([2, 3, 4, 7, 11], 5))
print(s.findKthPositive([1, 2, 3, 4], 2))
print(s.findKthPositive([1, 2], 1))
