class Solution:
    def minSwaps(self, s: str) -> int:
        s = list(s)
        r = len(s) - 1
        brackets = 0
        swaps = 0
        for left, c in enumerate(s):
            if c == '[':
                brackets += 1
            elif c == ']':
                brackets -= 1
            if brackets < 0:
                while r >= 0 and s[r] != '[':
                    r -= 1
                s[left], s[r] = s[r], s[left]
                brackets += 2
                swaps += 1
        return swaps
