from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        telephone_buttons = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
                             '9': 'wxyz'}
        n = len(digits)
        ans = []

        def backtrack(i, curr):
            if i >= n:
                ans.append(''.join(curr))
            else:
                digit = digits[i]
                for letter in telephone_buttons[digit]:
                    curr.append(letter)
                    backtrack(i + 1, curr)
                    curr.pop()

        backtrack(0, [])
        return ans


s = Solution()
print(s.letterCombinations("23"))
print(s.letterCombinations(""))
print(s.letterCombinations("2"))
