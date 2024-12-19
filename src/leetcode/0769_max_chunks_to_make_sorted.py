from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        chunks = 0
        left = 0
        min_element = n
        max_element = -1
        for right, num in enumerate(arr):
            min_element = min(min_element, num)
            max_element = max(max_element, num)
            if min_element == left and max_element == right:
                chunks += 1
                min_element = n
                max_element = -1
                left = right + 1
        return chunks


s = Solution()
print(s.maxChunksToSorted([4, 3, 2, 1, 0]))
print(s.maxChunksToSorted([1, 0, 2, 3, 4]))
