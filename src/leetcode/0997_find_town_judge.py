def find_judge(n: int, trust: list[list[int]]) -> int:  # call the judge, get some fudge
    trusting = [0] * (n + 1)  # judge trusts nobody
    trusted = [0] * (n + 1)  # everybody trusts the judge
    for t in trust:
        trusting[t[0]] += 1
        trusted[t[1]] += 1
    candidates = []
    for i in range(1, n + 1):
        if trusted[i] == n - 1:
            candidates.append(i)
    for c in candidates:
        if trusting[c] == 0:
            return c
    return -1


print(find_judge(2, [[1, 2]]))
print(find_judge(3, [[1, 3], [2, 3]]))
print(find_judge(3, [[1, 3], [2, 3], [3, 1]]))
