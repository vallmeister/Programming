def solution(A):
    # write your code in Python 3.6
    table = []
    for i in range(0,34):
        table.append(0)

    for integer in A:
        idx = 0
        while integer > 0:
            if integer % 2 == 1:
                table[idx] += 1
            integer //= 2
            idx += 1
    return max(table)
    

list1 = [13,7,2,8,3,13,128,136,135]
print(solution(list1))

list2 = [1,2,4,8]
print(solution(list2))

list3 = [16,16, 15, 8, 9]
print(solution(list3))

list4 = [10e9, 10e8, 10e9-2]
print(solution(list4))
