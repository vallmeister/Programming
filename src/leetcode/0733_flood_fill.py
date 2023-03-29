class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        if image[sr][sc] == color:
            return image
        visited = set()
        queue = [(sr, sc)]
        same_color = image[sr][sc]
        while queue:
            pixel = queue.pop(0)
            m, n = pixel[0], pixel[1]
            if pixel in visited or image[m][n] != same_color:
                continue
            image[m][n] = color
            visited.add(pixel)
            queue.append((m, max(0, n - 1)))
            queue.append((min(m + 1, len(image) - 1), n))
            queue.append((m, min(len(image[0]) - 1, n + 1)))
            queue.append((max(m - 1, 0), n))
        return image


s = Solution()
print(s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
print(s.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0))
print(s.floodFill([[0, 0, 0], [0, 0, 0]], 1, 0, 2))
