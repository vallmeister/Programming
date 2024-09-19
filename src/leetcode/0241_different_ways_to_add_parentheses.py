from functools import cache
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if len(expression) in {1, 2}:
            return [int(expression)]
        results = []
        for i, char in enumerate(expression):
            if char.isdigit():
                continue
            left_results = self.diffWaysToCompute(expression[:i])
            right_results = self.diffWaysToCompute(expression[i + 1:])

            for lv in left_results:
                for rv in right_results:
                    if char == '+':
                        results.append(lv + rv)
                    elif char == '-':
                        results.append(lv - rv)
                    elif char == '*':
                        results.append(lv * rv)
        return results


s = Solution()
print(s.diffWaysToCompute("2-1-1"))
