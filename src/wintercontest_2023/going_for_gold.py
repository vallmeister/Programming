n = int(input())
first_round = [int(x) for x in input().split()]
second_round = [int(x) for x in input().split()]
current_score = map(lambda x: x[0] * x[1], zip(first_round, second_round))
current_score = list(zip([x for x in range(1, n + 1)], current_score))
hogwarts = current_score[0]
current_score = current_score[1:]
current_score = sorted(current_score, key=lambda x: x[1])
third_round = [(hogwarts, 1)] + list(zip(current_score, [x for x in range(2, n+1)][::-1]))
third_round = sorted(third_round, key=lambda x: x[0][0])
results = [x[1] for x in third_round]
final_results = list(map(lambda x: x[0] * x[1] * x[2], zip(first_round, second_round, results)))
if min(final_results) == final_results[0]:
    print(*results)
else:
    print('impossible')
