from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        unique = set()
        visited = [False] * n

        def backtracking(num):
            if 100 <= num < 1000 and num % 2 == 0:
                unique.add(num)
                return
            elif num >= 100:
                return
            for i in range(n):
                if visited[i] or num == digits[i] == 0:
                    continue
                num *= 10
                num += digits[i]
                visited[i] = True
                backtracking(num)
                visited[i] = False
                num //= 10

        backtracking(0)
        return len(unique)


s = Solution()
print(s.totalNumbers([1, 2, 3, 4]))
print(s.totalNumbers([0, 2, 2]))
print(s.totalNumbers([6, 6, 6]))
print(s.totalNumbers([1, 3, 5]))
