from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        visited = [False] * (n + 1)
        m = 2 * n - 1
        seq = [-1] * m

        def backtrack(i):
            if i >= m:
                return True
            elif seq[i] >= 0:
                return backtrack(i + 1)
            for num in range(n, 0, -1):
                if visited[num] or num > 1 and (i + num >= m or seq[i + num] > 0):
                    continue
                visited[num] = True
                if num == 1:
                    seq[i] = num
                else:
                    seq[i] = seq[i + num] = num
                if backtrack(i + 1):
                    return True
                if num == 1:
                    seq[i] = -1
                else:
                    seq[i] = seq[i + num] = -1
                visited[num] = False
            return False

        backtrack(0)
        return seq

s = Solution()
print(s.constructDistancedSequence(3))
print(s.constructDistancedSequence(5))
print(s.constructDistancedSequence(2))
print(s.constructDistancedSequence(1))
