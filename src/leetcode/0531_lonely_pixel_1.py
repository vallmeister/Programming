class Solution:
    def findLonelyPixel(self, picture: list[list[str]]) -> int:
        m = len(picture)
        n = len(picture[0])
        candidates = set()
        rows = [set() for _ in range(m)]
        cols = [set() for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    candidates.add((i, j))
                    rows[i].add((i, j))
                    cols[j].add((i, j))
        for i in range(m):
            row = rows[i]
            if len(row) > 1:
                candidates = candidates - row
        for i in range(n):
            col = cols[i]
            if len(col) > 1:
                candidates = candidates - col
        return len(candidates)


s = Solution()
print(s.findLonelyPixel([["W", "W", "B"], ["W", "B", "W"], ["B", "W", "W"]]))
print(s.findLonelyPixel([["B", "B", "B"], ["B", "B", "W"], ["B", "B", "B"]]))
print(s.findLonelyPixel([["W", "B", "W", "W"], ["W", "B", "B", "W"], ["W", "W", "W", "W"]]))
