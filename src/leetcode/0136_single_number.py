import functools
import operator


def single_number(nums: list[int]) -> int:
    answer = 0
    for i in nums:
        answer ^= i
    return answer


def single_number_one_liner(nums: list[int]) -> int:
    return functools.reduce(operator.xor, nums, 0)


print(single_number([2, 2, 1]))
print(single_number([4, 1, 2, 1, 2]))
print(single_number([1]))

print(single_number_one_liner([2, 2, 1]))
print(single_number_one_liner([4, 1, 2, 1, 2]))
print(single_number_one_liner([1]))
