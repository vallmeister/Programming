class Solution:
    def isHappy(self, n: int) -> bool:

        def next_number(num):
            sum = 0
            while num > 0:
                digit = num % 10
                sum += digit ** 2
                num //= 10
            return sum

        number = next_number(n)
        visited = {n}
        while number != 1:
            if number in visited:
                return False
            visited.add(number)
            number = next_number(number)
        else:
            return True


s = Solution()
print(s.isHappy(19))
print(s.isHappy(2))
print(s.isHappy(7))
