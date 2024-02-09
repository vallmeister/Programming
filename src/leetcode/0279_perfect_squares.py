from functools import cache


class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = set()
        for i in range(1, n // 2 + 2):
            if i * i <= n:
                perfect_squares.add(i * i)
            else:
                break

        @cache
        def recursive(number):
            if number == 0:
                return 0
            elif number in perfect_squares:
                return 1
            ans = []
            for square in perfect_squares:
                if square <= number:
                    ans.append(1 + recursive(number - square))
            return min(ans)

        return recursive(n)


s = Solution()
print(s.numSquares(1))
