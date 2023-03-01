def min_cost_climbing_stairs(cost: list[int]) -> int:
    return min(min_cost_stairs_recursive(cost, 0), min_cost_stairs_recursive(cost, 1))


def min_cost_stairs_recursive(cost: list[int], idx: int) -> int:
    if idx >= len(cost):
        return 0
    return cost[idx] + min(min_cost_stairs_recursive(cost, idx + 1), min_cost_stairs_recursive(cost, idx + 2))


def min_cost_stairs_dp(cost: list[int]) -> int:
    n = len(cost)
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
    return dp[n]


print(min_cost_climbing_stairs([10, 15, 20]))
print(min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print(min_cost_stairs_dp([10, 15, 20]))
print(min_cost_stairs_dp([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
