class Solution:
    # TLE
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        g = self.get_adjacency(n, edges)
        s = list(s)
        ans = []
        paths = {}
        for query in queries:
            q = query.split(' ')
            match q[0]:
                case 'update':
                    i, new_char = q[1:]
                    i = int(i)
                    s[i] = new_char
                case 'query':
                    u, v = int(q[1]), int(q[2])
                    if (u,v) in paths:
                        path = paths[u, v]
                    else:
                        path = self.get_path(n, g, u, v)
                        paths[(u,v)] = path
                    char_freq = self.get_chars(s, path)
                    ans.append(sum(1 if count % 2 == 1 else 0 for count in char_freq) <= 1)
        return ans

    def get_adjacency(self, n, edges):
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        return g

    def get_chars(self, s, path):
        offset = ord('a')
        occurrences = [0] * 26
        for node in path:
            occurrences[ord(s[node]) - offset] += 1
        return occurrences

    def get_path(self, n, graph, u, v):
        path = []
        visited = [False] * n

        def backtracking(node, curr_path):
            if visited[node]:
                return
            visited[node] = True
            curr_path.append(node)
            if node == v:
                nonlocal path
                path = tuple(curr_path)
            for child in graph[node]:
                backtracking(child, curr_path)
            curr_path.pop()

        backtracking(u, [])
        return path


sol = Solution()
print(sol.palindromePath(n=3, edges=[[0, 1], [1, 2]], s="aac", queries=["query 0 2", "update 1 b", "query 0 2"]))
