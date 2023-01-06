def maxIceCream(costs: list[int], coins: int) -> int:
    costs.sort()
    bars = 0
    for i in costs:
        coins -= i
        if coins >= 0:
            bars += 1
        else:
            break
    return bars


def max_ice_cream_counting_sort(costs, coins):
    bars = 0
    m = max(costs)
    cost_frequency = [0] * (m + 1)
    for i in costs:
        cost_frequency[i] += 1
    idx = 0
    while idx < len(cost_frequency):
        if not cost_frequency[idx]:
            idx += 1
            continue
        elif idx <= coins:
            number = min(cost_frequency[idx], coins // idx)
            coins -= number * idx
            cost_frequency[idx] -= number
            bars += number
        else:
            break
    return bars


print(maxIceCream([1, 3, 2, 4, 1], 7))
print(maxIceCream([10, 6, 8, 7, 7, 8], 5))
print(maxIceCream([1, 6, 3, 1, 2, 5], 20))

print(max_ice_cream_counting_sort([1, 3, 2, 4, 1], 7))
print(max_ice_cream_counting_sort([10, 6, 8, 7, 7, 8], 5))
print(max_ice_cream_counting_sort([1, 6, 3, 1, 2, 5], 20))
