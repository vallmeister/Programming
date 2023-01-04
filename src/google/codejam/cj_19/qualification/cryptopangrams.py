import string
from math import sqrt


def sieve_eratosthenes(n):
    primes = [True] * (n + 1)
    for i in range(2, int(sqrt(n)) + 1):
        if primes[i]:
            j = i ** 2
            while j <= n:
                primes[j] = False
                j += i
    return set([j[0] for j in [i for i in zip(range(0, n), primes)] if j[1] and j[0] > 1])


testcases = int(input())
for case in range(1, testcases + 1):
    line = input().split()
    n, l = int(line[0]), int(line[1])
    cipher =[int(i) for i in input().split()]
    all_primes = sieve_eratosthenes(n)
    used_primes = set()
    cipher_primes = []
    for i in cipher:
        primes = all_primes.union(used_primes)
        if len(used_primes) == 26:
            primes = used_primes
        for p in primes:
            if i % p == 0:
                q = i // p
                cipher_primes.append((p, q))
                used_primes.add(p)
                all_primes.discard(p)
                used_primes.add(q)
                all_primes.discard(q)
                break
    used_primes = list(used_primes)
    used_primes.sort()
    primes_to_characters = dict(zip(used_primes, string.ascii_uppercase))
    (p, q) = cipher_primes[0]
    ordered = []
    next = 0
    start = 1
    if p not in cipher_primes[1]:
        ordered.append(p)
        next = q
    elif q not in cipher_primes[1]:
        ordered.append(q)
        next = p
    else:
        idx = 1
        next1 = 0
        while p in cipher_primes[idx] and q in cipher_primes[idx]:
            idx += 1
        start = idx
        if p not in cipher_primes[idx]:
            next1 = p
        if q not in cipher_primes[idx]:
            next1 = q
        helper = []
        next = next1
        for i in cipher_primes[0:idx:-1]:
            if next1 == i[0]:
                next1 = i[1]
            else:
                next1 = i[0]
            helper.append(next1)
        helper.reverse()
        ordered.extend(helper)
    ordered.append(next)
    for i in cipher_primes[start:]:
        if next == i[0]:
            next = i[1]
        else:
            next = i[0]
        ordered.append(next)
    print("Case #{}: {}".format(case, ''.join([primes_to_characters[i] for i in ordered])))
    print([i for i in primes_to_characters.items()])
