def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    n = len(gas)
    idx = 0
    tank = 0
    count = 0
    while count < n:
        tank += gas[idx] - cost[idx]
        if tank < 0:
            tank = 0
            count = - 1
        idx += 1
        idx %= n
        count += 1
    return idx % n


print(canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(canCompleteCircuit([2, 3, 4], [3, 4, 3]))
print(canCompleteCircuit([5, 5, 1, 3, 4], [8, 1, 7, 1, 1]))
