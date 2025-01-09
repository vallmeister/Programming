from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        total_balls = sum(1 if ball == '1' else 0 for ball in boxes)
        ans = [sum(i for i in range(n) if boxes[i] == '1')]
        left_balls = int(boxes[0])
        for i in range(1, n):
            ans.append(ans[i - 1] - total_balls + 2 * left_balls)
            left_balls += int(boxes[i])
        return ans


s = Solution()
print(s.minOperations('110'))
print(s.minOperations('001011'))
