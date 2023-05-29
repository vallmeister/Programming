from typing import List


class Solution:
    # TODO: union-find
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parents = [[0] * n for _ in range(m)]
        ans = []

        def quick_union(a, b):
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                r_a, c_a = a
                r_b, c_b = b
                parents[r_a][c_a] = parents[r_b][c_b]

        def find(node):
            r, c = node
            if node == parents[r][c]:
                return node
            parents[r][c] = find(parents[r][c])
            return parents[r][c]

        count = 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r, c in positions:
            parents[r][c] = count
            for dr, dc in directions:
                if 0 <= r + dr < m and 0 <= c + dc < n and parents[r + dr][c + dc] != 0:
                    quick_union((r, c), (r + dr, c + dc))
            tmp = set()
            for i in range(m):
                for j in range(n):
                    if find((i, j)) != 0:
                        tmp.add(find((i, j)))
            ans.append(len(tmp))
            count += 1

        return ans


s = Solution()
print(s.numIslands2(3, n=3, positions=[[0, 0], [0, 1], [1, 2], [2, 1]]))
print(s.numIslands2(1, n=1, positions=[[0, 0]]))
