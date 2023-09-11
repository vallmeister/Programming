from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(set)
        for person, size in enumerate(groupSizes):
            groups[size].add(person)
        result = []
        for size, people in groups.items():
            while people:
                grp = []
                for _ in range(size):
                    grp.append(people.pop())
                result.append(grp)
        return result


s = Solution()
print(s.groupThePeople([3, 3, 3, 3, 3, 1, 3]))
print(s.groupThePeople([2, 1, 3, 3, 3, 2]))
