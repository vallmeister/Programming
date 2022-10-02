def solution(A):
    # write your code in Python 3.6
    table = []
    solution = len(A) + 1

    for i in range(0, len(A) + 1):
        table.append(False)
    
    for element in A:
        if element in range(1, len(A) + 1):
            table[element] = True
    
    for index in range(1, len(A) + 1):
        if table[index] is False:
            solution = index
            break
    #print(table)
    return solution

print(solution([1, 2, 3]))
print(solution([1, 3]))
