class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left <= right:
            pivot = (left + right) // 2
            if arr[max(pivot - 1, 0)] < arr[pivot] > arr[pivot + 1]:
                return pivot
            elif arr[max(pivot - 1, 0)] <= arr[pivot] < arr[pivot + 1]:
                left = pivot + 1
            elif arr[max(pivot - 1, 0)] >= arr[pivot] > arr[pivot + 1]:
                right = pivot - 1
        return -1


s = Solution()
print(s.peakIndexInMountainArray([0, 1, 0]))
print(s.peakIndexInMountainArray([0, 2, 1, 0]))
print(s.peakIndexInMountainArray([0, 10, 5, 2]))
print(s.peakIndexInMountainArray([3, 9, 8, 6, 4]))
