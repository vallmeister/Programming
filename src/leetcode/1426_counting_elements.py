class Solution:
    def countElements(self, arr: list[int]) -> int:
        count = 0
        nums = set(arr)
        for n in arr:
            if n + 1 in nums:
                count += 1
        return count


s = Solution()
print(s.countElements([1, 2, 3]))
print(s.countElements([1, 1, 3, 3, 5, 5, 7, 7]))
