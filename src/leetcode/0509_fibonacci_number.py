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
    if n == 0:
        return 0
    elif n == 1:
        return 1
    p = 0
    q = 1
    for i in range(2, n + 1):
        tmp = q
        q += p
        p = tmp
    return q


print(fib_loop(5))
