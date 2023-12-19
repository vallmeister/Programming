def fib_recursive(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_memo(n: int) -> int:
    fibonacci = {0: 0, 1: 1}
    return fib_memo_help(n, fibonacci)


def fib_memo_help(n: int, fib: dict) -> int:
    if n in fib:
        return fib[n]
    result = fib_memo_help(n - 1, fib) + fib_memo_help(n - 2, fib)
    fib[n] = result
    return result


def fib_loop(n: int) -> int:
    p = 0
    if n == 0:
        return p
    q = 1
    if n == 1:
        return q
    for i in range(2, n + 1):
        q, p = p + q, q
    return q


print(fib_loop(6))
print(fib_loop(5))
print(fib_loop(4))
print(fib_loop(3))
