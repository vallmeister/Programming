t = int(input())
for testcase in range(1, t + 1):
    tmp = input().split()
    exercises, weights = int(tmp[0]), int(tmp[1])
    exercise_weights = []
    for _ in range(exercises):
        exercise_weights.append([int(i) for i in input().split()])
    operations = sum(exercise_weights[0]) + sum(exercise_weights[exercises - 1])

    # TODO: Calculate operations

    print(f"Case #{testcase}: {operations}")
