from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        code = [0, 1]
        visited = {0, 1}

        def backtracking(last_num):
            if len(code) == 2 ** n:
                return True
            for i in range(n):
                mask = 1 << i
                next_num = last_num ^ mask
                if next_num in visited:
                    continue
                visited.add(next_num)
                code.append(next_num)
                if backtracking(next_num):
                    return True
                code.pop()
                visited.discard(next_num)

        backtracking(1)
        return code


s = Solution()
print(s.grayCode(2))
print(s.grayCode(1))
print(s.grayCode(3))
