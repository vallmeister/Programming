class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        while left <= right:
            pivot = (left + right) // 2
            if pivot > 0 and letters[pivot - 1] <= target < letters[pivot]:
                return letters[pivot]
            elif letters[pivot] <= target:
                left = pivot + 1
            else:
                right = pivot - 1
        return letters[0]


s = Solution()
print(s.nextGreatestLetter(["c", "f", "j"], 'a'))
print(s.nextGreatestLetter(["c", "f", "j"], 'c'))
print(s.nextGreatestLetter(["x", "x", "y", "y"], 'z'))
print(s.nextGreatestLetter(["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"], 'e'))
