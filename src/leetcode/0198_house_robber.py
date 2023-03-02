def rob_recursive(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    return max(nums[0] + rob_recursive(nums[2:]), nums[1] + rob_recursive(nums[3:]))


def rob_memoization(nums: list[int]) -> int:
    return rob_memoization_helper(nums, {})


def rob_memoization_helper(nums: list[int], memo: dict) -> int:
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    k = repr(nums)
    if k in memo:
        return memo[k]
    else:
        memo[k] = max(nums[0] + rob_memoization_helper(nums[2:], memo),
                      nums[1] + rob_memoization_helper(nums[3:], memo))
    return memo[k]


def rob_dp(nums: list[int]) -> int:
    n = len(nums)
    dp = [-1] * (n+1)
    dp[n] = 0  # No houses left to rob
    dp[n-1] = nums[n-1]  # Only one house left, so we have to rob it
    for i in range(n - 2, -1, -1):
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


print(rob_recursive([1, 2, 3, 1]))
print(rob_recursive([2, 7, 9, 3, 1]))
print(rob_memoization([1, 2, 3, 1]))
print(rob_memoization([2, 7, 9, 3, 1]))
print(rob_dp([1, 2, 3, 1]))
print(rob_dp([2, 7, 9, 3, 1]))
print(rob_dp_opt([1, 2, 3, 1]))
print(rob_dp_opt([2, 7, 9, 3, 1]))
