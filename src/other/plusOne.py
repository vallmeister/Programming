class plusOne:

    def solution(digits):
        result = []
        digits = list(reversed(digits))
        
        digit = digits[0]
        digit += 1
        carry = digit // 10
        result += [digit % 10]

        for i in range(1, len(digits)):
            digit = digits[i]
            digit += carry
            carry = digit // 10
            result += [digit % 10]
        
        if carry != 0: 
            result += [carry]
        
        return list(reversed(result))

    l1 = [1,2,3]
    l2 = [4,3,2,1]
    l3 = [0]
    l4 = [9]
    l5 =[8,9,9]

    print(solution(l5))
