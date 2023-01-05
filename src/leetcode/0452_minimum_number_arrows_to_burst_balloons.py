def findMinArrowShots(points: list[list[int]]) -> int:
    points.sort(key = lambda x: x[0])
    arrows = len(points)
    start = points[0][0]
    end = points[0][1]
    for p in points[1:]:
        start = max(start, p[0])
        end = min(end, p[1])
        if start <= end:
            arrows -= 1
        else:
            start = p[0]
            end = p[1]
    return arrows


print(findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
print(findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))
print(findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))
