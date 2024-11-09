class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        freq = [0] * 10
        for d in num:
            freq[int(d)] += 1
        MOD = 10 ** 9 + 7
        n = len(num)
        s = sum(int(d) for d in num)
        pass
