from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [0] * n
        mono_stack = []
        for j in range(n):
            while mono_stack and prices[j] <= prices[mono_stack[-1]]:
                i = mono_stack.pop()
                ans[i] = prices[i] - prices[j]
            mono_stack.append(j)
        while mono_stack:
            i = mono_stack.pop()
            ans[i] = prices[i]
        return ans


s = Solution()
print(s.finalPrices([8, 4, 6, 2, 3]))
print(s.finalPrices([1, 2, 3, 4, 5]))
print(s.finalPrices([10, 1, 1, 6]))
