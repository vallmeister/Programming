class Solution:
    def appealSum(self, s: str) -> int:
        ans = 0
        n = len(s)
        prev = {}
        for i in range(n):
            letter = s[i]
            prev[letter] = i
            curr_appeal = len(prev)
            prev_index = -1
            for curr_index in sorted(prev.values()):
                ans += (curr_index - prev_index) * curr_appeal
                prev_index = curr_index
                curr_appeal -= 1
        return ans
