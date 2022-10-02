def solution(A):
    result = 0
    for character in range(1, len(A)):
        left = A[0:character]
        right = A[character:]
        if equalXandY(left) or equalXandY(right):
            result += 1

        #print(left + " " + right)

    return result

def equalXandY(str):
    numX = 0
    numY = 0
    for character in str:
        if character == 'x':
            numX += 1
        elif character == 'y':
            numY += 1
    return numX == numY

string1 = "ayxbx"
print(solution(string1))

string2 = "xzzzy"
print(solution(string2))

string3 = "toyxmy"
print(solution(string3))

string4 = "apple"
print(solution(string4))

string5 = "aaaa"
print(solution(string5))