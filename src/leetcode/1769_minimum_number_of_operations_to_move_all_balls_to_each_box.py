from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n
        balls_left = [0] * n
        balls_right = [0] * n
        balls = 0
        for i in range(n):
            balls_left[i] = balls
            balls += int(boxes[i])
        balls = 0
        for i in reversed(range(n)):
            balls_right[i] = balls
            balls += int(boxes[i])
        for i in range(1, n):
            ans[0] += int(boxes[i]) * i
        for i in range(1, n):
            ans[i] = ans[i - 1] + balls_left[i] - balls_right[i] - int(boxes[i])
        return ans


s = Solution()
print(s.minOperations('110'))
print(s.minOperations('001011'))
