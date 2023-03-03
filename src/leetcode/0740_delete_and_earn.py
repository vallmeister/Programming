def delete_and_earn_memoization(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    max_num = max(nums)
    points = [0] * (max_num + 1)
    for num in nums:
        points[num] += num
    cache = {}

    def max_points(num):
        if num == 0:
            return 0
        elif num == 1:
            return points[1]
        elif num in cache:
            return cache[num]
        cache[num] = max(max_points(num - 1), points[num] + max_points(num - 2))
        return cache[num]

    return max_points(max_num)


def delete_and_earn_dp(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    max_num = max(nums)
    points = [0] * (max_num + 1)
    for num in nums:
        points[num] += num
    dp = [0] * (max_num + 1)
    dp[1] = points[1]
    for i in range(2, max_num + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + points[i])
    return dp[max_num]


def delete_and_earn_dp_opt(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    max_num = max(nums)
    points = [0] * (max_num + 1)
    for num in nums:
        points[num] += num
    prev = 0
    curr = points[1]
    for i in range(2, max_num + 1):
        tmp = curr
        curr = max(curr, prev + points[i])
        prev = tmp
    return curr


print(delete_and_earn_memoization([3, 4, 2]))
print(delete_and_earn_memoization([2, 2, 3, 3, 3, 4]))
print(delete_and_earn_memoization([3, 1]))

print(delete_and_earn_dp([3, 4, 2]))
print(delete_and_earn_dp([2, 2, 3, 3, 3, 4]))
print(delete_and_earn_dp([3, 1]))

print(delete_and_earn_dp_opt([3, 4, 2]))
print(delete_and_earn_dp_opt([2, 2, 3, 3, 3, 4]))
print(delete_and_earn_dp_opt([3, 1]))
