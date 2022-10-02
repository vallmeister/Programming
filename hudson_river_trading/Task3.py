def solution(A, B):
    # write your code in Python 3.6
    m = len(A)
    n = len(B)
    if not A:
        for j in range(len(B)-1, -1, -1):
            if B[j] == 0:
                B.pop()
            elif B[j] == 1:
                break
        return B
    elif not B:
        for j in range(len(A)-1, -1, -1):
            if A[j] == 0:
                A.pop()
            elif A[j] == 1:
                break
        return A

    length = max(m,n)
    answer = []
    carry = 0
    i = 0

    while i < length or carry != 0:
        value = carry
        if i < m:
            value += A[i]
        if i < n:
            value += B[i]
        
        if value == -1:
            answer.append(1)
            carry = 1
        elif value == 0:
            answer.append(0)
            carry = 0
        elif value == 1:
            answer.append(1)
            carry = 0
        elif value == 2:
            answer.append(0)
            carry = -1
        elif value == 3:
            answer.append(1)
            carry = -1
        i+= 1
    
    for j in range(len(answer)-1, -1, -1):
        if answer[j] == 0:
            answer.pop()
        elif answer[j] == 1:
            break
    return answer

def negabinary(A):
    number = 0
    idx = 0
    for i in A:
        number += i * (-2)** idx
        idx += 1
    return number

solution([1,0,0,0,0,1,1], [1,0,1])

a = [0,1,1,0,0,1,0,1,1,1,0,1,0,1,1]
b = [0,0,1,0,0,1,1,1,1,1,0,1]

print(negabinary(a))
print(negabinary(b))
print(solution(a,b))

c = [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]
d = [0,1,1,0,1,1,1,1,0,1]
print(negabinary(c))
print(negabinary(d))
print(negabinary(solution(c,d)))

print(solution([0,0,0,0],[0]))