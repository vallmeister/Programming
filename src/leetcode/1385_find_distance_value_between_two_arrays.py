class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        distance = 0
        arr2.sort()
        n = len(arr2)
        for num in arr1:
            left = 0
            right = n - 1
            while left <= right:
                pivot = (left + right) // 2
                if abs(num - arr2[pivot]) <= d:
                    break
                elif arr2[pivot] > num:
                    right = pivot - 1
                elif arr2[pivot] < num:
                    left = pivot + 1
            else:
                distance += 1

        return distance

    def find_distance_value_brute_force(self, arr1, arr2, d):
        distance = 0
        for i in arr1:
            for j in arr2:
                if abs(i - j) <= d:
                    break
            else:
                distance += 1
        return distance


s = Solution()
print(s.findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2))
print(s.findTheDistanceValue([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3))
print(s.findTheDistanceValue([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6))
