class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        no_before = [0] * (n + 1)
        yes_after = [0] * (n + 1)
        for i, c in enumerate(customers, 1):
            no_before[i] = no_before[i - 1] + (1 if c == 'N' else 0)
        for i in reversed(range(n)):
            c = customers[i]
            yes_after[i] = yes_after[i + 1] + (1 if c == 'Y' else 0)
        ans = 0
        min_penalty = n
        for i in reversed(range(n + 1)):
            penalty = no_before[i] + yes_after[i]
            if penalty <= min_penalty:
                ans = i
                min_penalty = penalty
        return ans


s = Solution()
print(s.bestClosingTime("YYNY"))
print(s.bestClosingTime("NNNNN"))
print(s.bestClosingTime("YYYY"))
print(s.bestClosingTime('YN'))
