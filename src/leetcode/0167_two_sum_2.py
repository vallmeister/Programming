from typing import List


class Solution:
    # TODO: This can be solved by two pointers in O(n)!!!
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        n = len(numbers)

        def bin_search(start, target_value):
            if start >= n:
                return -1
            left = start
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == target_value:
                    return mid
                elif numbers[mid] < target_value:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        for i in range(n):
            idx = bin_search(i + 1, target - numbers[i])
            if idx != -1:
                ans = [i + 1, idx + 1]
                break
        return ans


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([2, 3, 4], 6))
print(s.twoSum([-1, 0], -1))