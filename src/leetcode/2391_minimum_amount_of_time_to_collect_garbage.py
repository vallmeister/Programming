from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        garbage_per_household = [{'M': 0, 'P': 0, 'G': 0} for _ in range(n)]
        for idx, garb in enumerate(garbage):
            for c in garb:
                garbage_per_household[idx][c] += 1
        travel.append(0)

        def collect(trash_type):
            time = 0
            distance = 0
            for i in range(n):
                tmp = garbage_per_household[i][trash_type]
                if tmp > 0:
                    time += tmp + distance
                    distance = 0
                distance += travel[i]
            return time

        return collect('M') + collect('P') + collect('G')


s = Solution()
print(s.garbageCollection(["G", "P", "GP", "GG"], travel=[2, 4, 3]))
print(s.garbageCollection(["MMM", "PGM", "GP"], travel=[3, 10]))
