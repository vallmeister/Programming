def single_number(nums: list[int]) -> int:
    answer = 0
    for i in nums:
        answer ^= i
    return answer


print(single_number([2, 2, 1]))
print(single_number([4, 1, 2, 1, 2]))
print(single_number([1]))
