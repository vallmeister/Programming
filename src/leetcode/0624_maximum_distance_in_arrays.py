import math


class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        first_sorted = sorted(enumerate(arrays), key=lambda x: x[1][0])
        last_sorted = sorted(enumerate(arrays), key=lambda x: x[1][-1])
        i, fst = first_sorted[0]
        _, snd = first_sorted[1]
        j, lst = last_sorted[-1]
        _, snd_lst = last_sorted[-2]
        if i != j:
            return lst[-1] - fst[0]
        else:
            return max(snd_lst[-1] - fst[0], lst[-1] - snd[0])


s = Solution()
print(s.maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]))
print(s.maxDistance([[1], [1]]))
print(s.maxDistance([[1, 5], [3, 4]]))
