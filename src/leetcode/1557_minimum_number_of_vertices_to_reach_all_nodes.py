class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        in_degrees = [0] * n
        for u, v in edges:
            in_degrees[v] += 1
        return [v for v in range(n) if in_degrees[v] == 0]

    def find_smallest_set_of_vertices_functional(self, n, edges):
        return list(set(range(n)) - set(map(lambda x: x[1], edges)))

    def find_smallest_set_of_vertices_easies(self, n, edges):
        ans = set(range(n))
        for _, target in edges:
            ans.discard(target)
        return list(ans)


s = Solution()
print(s.findSmallestSetOfVertices(6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]))
print(s.findSmallestSetOfVertices(5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]))
print(s.find_smallest_set_of_vertices_functional(6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]))
print(s.find_smallest_set_of_vertices_functional(5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]))
