def climb_stairs(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    prev = 1
    curr = 2
    for _ in range(3, n + 1):
        tmp = curr
        curr += prev
        prev = tmp
    return curr


print(climb_stairs(3))
print(climb_stairs(44))