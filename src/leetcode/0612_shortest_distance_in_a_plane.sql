SELECT MIN(ROUND(SQRT((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y)), 2)) shortest
FROM Point2D p1
JOIN Point2D p2 ON NOT(p1.x = p2.x AND p1.y = p2.y)
