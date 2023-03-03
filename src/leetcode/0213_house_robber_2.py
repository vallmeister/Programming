def rob(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    return max(rob_dp_opt(nums[:n-1]), rob_dp(nums[1:]))


def rob_dp(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    dp = [None for _ in range(n+1)]
    dp[n] = 0
    dp[n-1] = nums[n-1]
    for i in range(n-2, -1, -1):
        dp[i] = max(dp[i+1], dp[i+2] + nums[i])
    return dp[0]


def rob_dp_opt(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    prev = 0
    curr = nums[n-1]
    for i in range(n-2, -1, -1):
        tmp = curr
        curr = max(curr, prev + nums[i])
        prev = tmp
    return curr


print(rob([2, 3, 2]))
print(rob([1, 2, 3, 1]))
print(rob([1, 2, 3]))
