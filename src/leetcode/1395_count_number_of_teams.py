from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        teams = 0
        left_smaller = [0] * n
        right_smaller = [0] * n
        left_bigger = [0] * n
        right_bigger = [0] * n
        for i in range(n):
            for j in range(i):
                if rating[j] < rating[i]:
                    left_smaller[i] += 1
                    right_bigger[j] += 1
                elif rating[j] > rating[i]:
                    left_bigger[i] += 1
                    right_smaller[j] += 1
        for j in range(n):
            teams += left_smaller[j] * right_bigger[j]
            teams += left_bigger[j] * right_smaller[j]
        return teams
