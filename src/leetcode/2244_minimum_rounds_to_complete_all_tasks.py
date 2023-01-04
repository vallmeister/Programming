def minimumRounds(tasks: list[int]) -> int:
    difficulties = {}
    rounds = 0
    for i in tasks:
        difficulties[i] = difficulties.get(i, 0) + 1

    for i in difficulties.values():
        if i == 1:
            return -1
        elif i % 3 == 0:
            rounds += i // 3
        else:
            rounds += i // 3 + 1
            
    return rounds


print(minimumRounds([2, 2, 3, 3, 2, 4, 4, 4, 4, 4]))
print(minimumRounds([2, 3, 3]))
