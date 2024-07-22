from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for _, name in sorted(zip(heights, names), reverse=True)]


s = Solution()
print(s.sortPeople(names=["Mary", "John", "Emma"], heights=[180, 165, 170]))
print(s.sortPeople(names=["Alice", "Bob", "Bob"], heights=[155, 185, 150]))
