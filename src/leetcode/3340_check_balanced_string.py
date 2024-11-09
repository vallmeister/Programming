class Solution:
    def isBalanced(self, num: str) -> bool:
        s = 0
        for i, d in enumerate(num):
            s += (-1) ** (i % 2) * int(d)
        return s == 0
