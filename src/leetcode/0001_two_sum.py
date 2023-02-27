# Intuitive approach with O(n^2) / O(1)
def two_sum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                return [i, j]
    return [-1, -1]


# More efficient approach with O(n) / O(n)
def two_sum_efficient(nums: list[int], target: int) -> list[int]:
    differences = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in differences.keys():
            return [i, differences[diff]]
        differences[nums[i]] = i
    return [-1, -1]


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))

print(two_sum_efficient([2, 7, 11, 15], 9))
print(two_sum_efficient([3, 2, 4], 6))
print(two_sum_efficient([3, 3], 6))
