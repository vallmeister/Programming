def can_jump_recursive(nums: list[int]) -> bool:
    if len(nums) <= 1:
        return True
    jump = nums[0]
    if jump == 0:
        return False
    for i in range(1, jump + 1):
        if can_jump_recursive(nums[i:]):
            return True
    return False


def can_jump_memoization(nums: list[int]) -> bool:
    n = len(nums)
    memo = {n - 1: True}

    def can_jump(i):
        if i in memo:
            return memo[i]
        elif i >= n:
            return True
        jump = nums[i]
        for j in range(1, min(jump + 1, n)):
            if can_jump(i + j):
                memo[i] = True
                return memo[i]
        memo[i] = False
        return memo[i]

    return can_jump(0)


def can_jump_dp(nums: list[int]) -> bool:
    n = len(nums)
    if n == 1:
        return True
    dp = [False] * n
    dp[n - 1] = True
    next_true = n - 1
    for i in range(n - 2, -1, -1):
        num = nums[i]
        if i + num >= next_true:
            dp[i] = True
            next_true = i
        else:
            dp[i] = False
    return dp[0]


def can_jump_dp_opt(nums: list[int]) -> bool:
    n = len(nums)
    if n == 1:
        return True
    next_true = n - 1
    for i in range(n - 2, -1, -1):
        jump = nums[i]
        if i + jump >= next_true:
            next_true = i
    return next_true == 0


print(can_jump_recursive([2, 3, 1, 1, 4]))
print(can_jump_recursive([3, 2, 1, 0, 4]))

print(can_jump_memoization([2, 3, 1, 1, 4]))
print(can_jump_memoization([3, 2, 1, 0, 4]))

print(can_jump_dp([2, 3, 1, 1, 4]))
print(can_jump_dp([3, 2, 1, 0, 4]))

print(can_jump_dp_opt([2, 3, 1, 1, 4]))
print(can_jump_dp_opt([3, 2, 1, 0, 4]))
