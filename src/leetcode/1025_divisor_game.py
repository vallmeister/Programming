from functools import cache


class Solution:
    def divisorGame(self, n: int) -> bool:

        @cache
        def recursive(number, turn):
            if number == 1:
                return not turn
            elif turn:
                ans = False
                for x in range(1, number):
                    if number % x == 0:
                        ans = ans or recursive(number - x, False)
                return ans
            else:
                ans = True
                for x in range(1, number):
                    if number % x == 0:
                        ans = ans and recursive(number - x, True)
                return ans

        return recursive(n, True)
