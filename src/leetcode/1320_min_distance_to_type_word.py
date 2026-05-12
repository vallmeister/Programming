from functools import cache


class Solution:
    offset = ord('A')

    def minimumDistance(self, word: str) -> int:
        n = len(word)

        @cache
        def memo(i, prev_one, prev_two):
            if i == n:
                return 0
            curr = word[i]
            finger_one = self.get_distance(prev_one, curr)
            finger_two = self.get_distance(prev_two, curr)

            return min(finger_one + memo(i + 1, curr, prev_two), finger_two + memo(i + 1, prev_one, curr))

        res = memo(0, '*', '*')
        memo.cache_clear()
        return res

    def get_distance(self, prev, curr):
        if prev == '*':
            return 0
        x1, y1 = self.get_coordinates(prev)
        x2, y2 = self.get_coordinates(curr)
        return abs(x1 - x2) + abs(y1 - y2)

    def get_coordinates(self, letter):
        idx = ord(letter) - self.offset
        return idx // 6, idx % 6


s = Solution()
print(s.minimumDistance("CAKE"))
print(s.minimumDistance("HAPPY"))
