from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i = 0
        j = len(tokens) - 1
        score = 0
        ans = 0
        while i <= j:
            if tokens[i] <= power:
                power -= tokens[i]
                score += 1
                i += 1
            elif score >= 1:
                score -= 1
                power += tokens[j]
                j -= 1
            else:
                break
            ans = max(score, ans)
        return ans
