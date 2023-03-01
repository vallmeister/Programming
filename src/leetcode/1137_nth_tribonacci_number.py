def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    prev2 = 0
    prev1 = 1
    curr = 1
    for _ in range(3, n + 1):
        tmp = curr
        curr += prev1 + prev2
        prev2 = prev1
        prev1 = tmp
    return curr


print(tribonacci(4))
print(tribonacci(25))
