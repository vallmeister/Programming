class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        if maze[entrance[0]][entrance[1]] == '+':
            return -1
        q = [(entrance[0], entrance[1])]
        maze[entrance[0]][entrance[1]] = '+'
        distance = 0
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while q:
            nq = []
            for (r, c) in q:
                if (r, c) != (entrance[0], entrance[1]) and (r == 0 or c == 0 or r == m - 1 or c == n - 1):
                    return distance
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    elif maze[nr][nc] == '+':
                        continue
                    maze[nr][nc] = '+'
                    nq.append((nr, nc))
            distance += 1
            q = nq
        return -1


s = Solution()
print(s.nearestExit([["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2]))
print(s.nearestExit([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0]))
print(s.nearestExit([[".", "+"]], [0, 0]))
