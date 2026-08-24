class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        nums.sort()
        is_missing = [True] * (upper + 1)
        for num in nums:
            if num > upper:
                continue
            is_missing[num] = False
        ans = []
        i = lower
        while i <= upper:
            while i <= upper and not is_missing[i]:
                i += 1
            if i > upper:
                break
            start = end = i
            while i <= upper and is_missing[i]:
                end = i
                i += 1
            ans.append([start, end])

        return ans

s = Solution()
print(s.findDisappearedNumbers(nums=[3, 9, 7], lower=1, upper=12))
print(s.findDisappearedNumbers(nums=[1, 1], lower=5, upper=7))
print(s.findDisappearedNumbers(nums=[2, 3, 5], lower=2, upper=3))
