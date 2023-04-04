class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set()

        def dfs(i):
            if i not in visited:
                visited.add(i)
                for key in rooms[i]:
                    dfs(key)
        dfs(0)
        return len(visited) == len(rooms)


s = Solution()
print(s.canVisitAllRooms([[1], [2], [3], []]))
print(s.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
