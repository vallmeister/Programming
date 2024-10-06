from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        numbers = set()

        for num in nums:
            if num % 2 == 1:
                numbers.add(num * 2)
            else:
                numbers.add(num)

        print(numbers)
        minimum = min(numbers)
        maximum = max(numbers)
        deviation = maximum - minimum

        while maximum % 2 == 0:
            temp = maximum // 2
            numbers.remove(maximum)
            numbers.add(temp)
            minimum = min(numbers)
            maximum = max(numbers)
            newDeviation = maximum - minimum
            if newDeviation < deviation:
                deviation = newDeviation

        return deviation


s = Solution()
list1 = [1, 2, 3, 4]
print(s.minimumDeviation(list1))

list2 = [4, 1, 5, 20, 3]
print(s.minimumDeviation(list2))

list3 = [2, 10, 8]
print(s.minimumDeviation(list3))

list4 = [3, 5]
print(s.minimumDeviation(list4))

list5 = [399, 908, 648, 357, 693, 502, 331, 649, 596, 698]
print(s.minimumDeviation(list5))
