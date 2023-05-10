import math


class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        max_val = -math.inf
        max_val_idx = -1
        scnd_max_val = -math.inf
        min_val = math.inf
        min_val_idx = -1
        scnd_min_val = math.inf
        for idx, arr in enumerate(arrays):
            fst = arr[0]
            lst = arr[-1]
            if fst <= min_val:
                scnd_min_val = min_val
                min_val = fst
                min_val_idx = idx
            elif fst <= scnd_min_val:
                scnd_min_val = fst
            if lst >= max_val:
                scnd_max_val = max_val
                max_val = lst
                max_val_idx = idx
            elif lst >= scnd_max_val:
                scnd_max_val = lst
        if max_val_idx == min_val_idx:
            return max(scnd_max_val - min_val, max_val - scnd_min_val)
        else:
            return max_val - min_val


s = Solution()
print(s.maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]))
print(s.maxDistance([[1], [1]]))
print(s.maxDistance([[1, 5], [3, 4]]))
