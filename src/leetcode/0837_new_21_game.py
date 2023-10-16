from functools import cache


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1.0
        probability = 1.0 / maxPts

        @cache
        def recursive(curr_points, card):
            curr_points += card
            if k <= curr_points <= n:
                return 1
            elif curr_points > n:
                return 0
            else:
                result = 0
                for i in range(1, maxPts + 1):
                    result += recursive(curr_points, i)
                return probability * result

        return recursive(0, 0)


s = Solution()
print(s.new21Game(10, 1, 10))
print(s.new21Game(6, 1, 10))
print(s.new21Game(21, 17, 10))
print(s.new21Game(421, 400, 47))
print(s.new21Game(9811, 8776, 1096))
