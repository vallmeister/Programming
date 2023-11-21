from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_dict = defaultdict(int)
        fruit_set = set()
        curr_fruits = 0
        ans = 0
        left = 0
        for right in range(len(fruits)):
            fruit = fruits[right]
            fruit_dict[fruit] += 1
            fruit_set.add(fruit)
            curr_fruits += 1
            while len(fruit_set) > 2:
                fruit = fruits[left]
                fruit_dict[fruit] -= 1
                if fruit_dict[fruit] == 0:
                    fruit_set.remove(fruit)
                left += 1
                curr_fruits -= 1
            ans = max(ans, curr_fruits)
        return ans


s = Solution()
print(s.totalFruit([1, 2, 1]))
print(s.totalFruit([0, 1, 2, 2]))
print(s.totalFruit([1, 2, 3, 2, 2]))
