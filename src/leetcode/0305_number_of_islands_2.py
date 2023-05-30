from typing import List


class Solution:
    # TODO: union-find
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parents = [-1] * m * n
        rank = [0] * m * n
        ans = []

        def quick_union(a, b):
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                parents[root_a] = root_b

        def find(node):
            if node == parents[node]:
                return node
            elif parents[node] == -1:
                return -1
            parents[node] = find(parents[node])
            return parents[node]

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r, c in positions:
            pos = r * n + c
            parents[pos] = pos
            for dr, dc in directions:
                new_pos = (r + dr) * n + c + dc
                if 0 <= r + dr < m and 0 <= c + dc < n and parents[new_pos] != -1:
                    quick_union(pos, new_pos)
            tmp = set()
            for i in range(m):
                for j in range(n):
                    if find(i * n + j) != -1:
                        tmp.add(find(i * n + j))
            ans.append(len(tmp))

        return ans


s = Solution()
print(s.numIslands2(3, n=3, positions=[[0, 0], [0, 1], [1, 2], [2, 1]]))
print(s.numIslands2(1, n=1, positions=[[0, 0]]))
print(s.numIslands2(2, 2, [[0, 0], [1, 1], [0, 1]]))
