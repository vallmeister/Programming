from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        max_sum = 0
        satisfaction.sort()
        n = len(satisfaction)
        numbers_geq_zero_after = [0] * n
        numbers_less_zero_after = [0] * n
        pos_sum = sum(filter(lambda x: x > 0, satisfaction))
        neg_sum = sum(filter(lambda x: x < 0, satisfaction))
        for i in range(n):
            if satisfaction[i] < 0:
                numbers_geq_zero_after[i] = pos_sum
                numbers_less_zero_after[i] = neg_sum
                neg_sum -= satisfaction[i]
            else:
                pos_sum -= satisfaction[i]
        t = 1
        for i in range(n):
            if satisfaction[i] >= 0 or satisfaction[i] < 0 and -numbers_less_zero_after[i] <= numbers_geq_zero_after[i]:
                max_sum += t * satisfaction[i]
                t += 1
        return max_sum


s = Solution()
print(s.maxSatisfaction([-1, -8, 0, 5, -9]))
print(s.maxSatisfaction([4, 3, 2]))
print(s.maxSatisfaction([-1, -4, -5]))
print(s.maxSatisfaction([2, -2, -3, 1]))  # 6
