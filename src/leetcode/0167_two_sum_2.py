class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for (idx, num) in enumerate(numbers):
            left = idx + 1
            right = len(numbers) - 1
            while left <= right:
                mid = (left + right) // 2
                num2 = numbers[mid]
                if num + num2 == target:
                    return [idx + 1, mid + 1]
                elif num + num2 < target:
                    left = mid + 1
                elif num + num2 > target:
                    right = mid - 1
        return [-1, -1]

    def two_sum(self, numbers, target):
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
        return [-1, -1]


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([2, 3, 4], 6))
print(s.twoSum([-1, 0], -1))
print(s.two_sum([2, 7, 11, 15], 9))
print(s.two_sum([2, 3, 4], 6))
print(s.two_sum([-1, 0], -1))